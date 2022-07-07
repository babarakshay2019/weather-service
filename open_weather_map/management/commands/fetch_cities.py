import gzip
import json
import urllib

from django.core.management import BaseCommand

from open_weather_map.models import City
from weather_service.settings import OPEN_WEATHER_MAP_CITY_LIST_URL


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        url = OPEN_WEATHER_MAP_CITY_LIST_URL
        f = urllib.request.urlopen(url)
        decompressed_data = gzip.decompress(f.read())
        cities_list = json.loads(decompressed_data)
        canadian_cities = [
            City(
                **{
                    "city_id": city["id"],
                    "name": city["name"],
                    "state": city["state"],
                    "country": city["country"],
                    "latitude": city["coord"]["lat"],
                    "longitude": city["coord"]["lon"],
                }
            )
            for city in cities_list
            if city["country"] == "CA"
        ]

        City.objects.bulk_create(canadian_cities, batch_size=4000)
        return "cities fetched successfully"
