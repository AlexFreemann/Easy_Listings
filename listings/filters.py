import django_filters
from .models import Listing
from django import forms


class ProductFilter(django_filters.FilterSet):
    check = forms.BooleanField(label="Check this")

    class Meta:
        model = Listing
        fields ={'price': ['lt', 'gt']}