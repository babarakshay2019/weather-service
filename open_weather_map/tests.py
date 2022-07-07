from cgi import test
from django.test import TestCase
from django.test.client import RequestFactory
from unittest.mock import MagicMock, patch
from django.test import client
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


# Create your tests here.
from open_weather_map.services import CallOpenWeatherMapAPI

class TestCallOpenWeatherMapAPI(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
    
    @patch('open_weather_map.services.make_action_request', MagicMock(return_value={"coord":{"lon": 106.3468, "lat": 56.1304}, "cod": 200}))
    def test_open_weather_api_response(self):
        request = self.factory.get("open-weather-   /cityweather")
        _mutable = request.GET._mutable
        request.GET._mutable = True
        request.GET["lat"] = 56.1304
        request.GET["lon"] = 106.3468
        data = CallOpenWeatherMapAPI.open_weather_map_data(request)
        assert data["coord"] == {"lon": 106.3468, "lat": 56.1304}
        assert data["cod"] == 200

class TestFetchWeatherDetailEndpoint(TestCase):

    def setUp(self):
        self.client = APIClient()
         
    @patch("open_weather_map.services.CallOpenWeatherMapAPI.open_weather_map_data", MagicMock(return_value={"coord":{"lon": 106.3468, "lat": 56.1304}, "cod": 200}))
    def test_fetch_weather_data_endpoint(self):
        response=self.client.get(reverse("fetch_city_weather_detail"), data={"lon": 106.3468, "lat": 56.1304})
        response= response.json() 
        assert response["weather_object"]["coord"] == {"lon": 106.3468, "lat": 56.1304}
        assert response["weather_object"]["cod"] == 200

    @patch("open_weather_map.services.CallOpenWeatherMapAPI.open_weather_map_data", MagicMock(return_value={'weather_object': {'cod': '400', 'message': 'Nothing to geocode'}}))
    def test_fetch_weather_data_with_wrong_input(self):
        response=self.client.get(reverse("fetch_city_weather_detail"), data={})
        assert response.json() == {'weather_object': {'weather_object': {'cod': '400', 'message': 'Nothing to geocode'}}}

        
    @patch("open_weather_map.services.CallOpenWeatherMapAPI.open_weather_map_data", MagicMock(return_value={'weather_object': {'cod': '400', 'message': 'Nothing to geocode'}}))
    def test_fetch_weather_data_with_not_long(self):
        response=self.client.get(reverse("fetch_city_weather_detail"), data={"lat": 71.12345})
        assert response.json() == {'weather_object': {'weather_object': {'cod': '400', 'message': 'Nothing to geocode'}}}


class TestWeatherCitiesListEndpoint(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_fetch_cities_list(self):
         response=self.client.get(reverse("fecth_cities_list"))
         assert response.status_code == 200
