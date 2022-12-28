from django_filters import rest_framework as rest_filters
from .models import Card
from rest_framework import filters


class CharFilterInFilter(rest_filters.BaseInFilter, rest_filters.CharFilter):
    pass


class CardFilter(rest_filters.FilterSet):
    """class for filtration by type, genre, year_min, year_max"""
    genre = CharFilterInFilter(field_name='genre', lookup_expr='in')
    type = CharFilterInFilter(field_name='type', lookup_expr='in')
    year = rest_filters.RangeFilter()

    class Meta:
        model = Card
        fields = ['genre', 'type', 'year']


class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('title_only'):
            return ['title']
        return super().get_search_fields(view, request)