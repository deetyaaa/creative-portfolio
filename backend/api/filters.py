import django_filters
from .models import Creator

class CreatorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    creative_fields = django_filters.CharFilter(method="filter_fields")

    def filter_fields(self, queryset, name, value):
        fields = value.split(",")
        return queryset.filter(creative_fields__contains=fields)

    class Meta:
        model  = Creator
        fields = ["name", "creative_fields"]