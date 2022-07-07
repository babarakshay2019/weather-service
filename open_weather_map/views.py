import requests
from django.core.cache import cache
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from open_weather_map.filters import EmployeeFilter
from open_weather_map.models import City
from open_weather_map.services import CallOpenWeatherMapAPI


class FetchCitiesView(ListView):
    """
    This class is used to list cities as well as for searching the cities.
    """

    template_name = "index.html"
    paginate_by = 10
    model = City

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Overriding context data method to render city data into index template.
        :param object_list:
        :param kwargs:
        :return: template context
        """
        try:
            context = super(FetchCitiesView, self).get_context_data(**kwargs)
            city_objects = cache.get("city_objects")  # Fetching the cached objects
            if city_objects is None:
                city_objects = City.objects.all()
                cache.set("city_objects", city_objects)  # Caching the queryset objects
            if self.request.GET.get("name"):
                context["city_objects"] = EmployeeFilter(
                    self.request.GET, queryset=city_objects
                ).qs
                return context
            paginator = Paginator(city_objects, self.paginate_by)
            page = self.request.GET.get("page")
            try:
                city_objects = paginator.page(page)
            except PageNotAnInteger:
                city_objects = paginator.page(1)
            except EmptyPage:
                city_objects = paginator.page(paginator.num_pages)
            context["city_objects"] = city_objects
            return context
        except ValueError:
            print({"error": "page value must be integer"})


class FetchCityDataView(APIView):
    """
    This class include get method to fetch data from open weather api.
    """

    def get(self, request):
        try:
            response = CallOpenWeatherMapAPI.open_weather_map_data(request)
            return Response({"weather_object": response}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
