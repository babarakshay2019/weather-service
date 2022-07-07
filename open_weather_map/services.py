import requests

from weather_service.settings import OPEN_WEATHER_MAP_API_KEY, OPEN_WEATHER_MAP_API_URL


def make_action_request(url, param):
    """
    This function is used to call the endpoint.
    """
    try:
        headers = {}
        response = requests.get(url, params=param, headers=headers)
        return response.json()
    except Exception as e:
        raise Exception({"error": str(e)})


class CallOpenWeatherMapAPI:
    @staticmethod
    def open_weather_map_data(request):
        """
        This function is created to fetch the weather data from visual crossing API.

        :param request: request object.
        :type request: object
        :return: Return the json of weatherData objects.
        :rtype: json
        """
        try:
            _mutable = request.GET._mutable
            request.GET._mutable = True
            request.GET["appid"] = OPEN_WEATHER_MAP_API_KEY
            url = OPEN_WEATHER_MAP_API_URL
            response = make_action_request(url, request.GET)
            return response
        except ValueError as e:
            return {"error": f"It must be integer value:{e}"}
        except Exception as e:
            return {"error": str(e)}
