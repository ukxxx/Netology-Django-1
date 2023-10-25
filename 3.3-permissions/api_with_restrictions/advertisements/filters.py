from django_filters import rest_framework as filters
from django_filters.rest_framework import DateFromToRangeFilter

from advertisements.models import Advertisement


class DateRangeFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ["created_at", "status"]
