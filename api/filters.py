from django_filters import rest_framework as django_filters
from .models import Book

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price",lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price",lookup_expr="lte")
    class Meta:
        model = Book
        fields = ['genre','min_price','max_price']