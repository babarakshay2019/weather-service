import django_filters

from .models import City


class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = City
        fields = {"name"}
