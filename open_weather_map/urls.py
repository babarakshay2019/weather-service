from django.urls import path

from .views import FetchCitiesView, FetchCityDataView

urlpatterns = [
    path("", FetchCitiesView.as_view(), name="fecth_cities_list"),
    path("cityweather", FetchCityDataView.as_view(), name="fetch_city_weather_detail"),
]
