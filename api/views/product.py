from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from api.models import Book,Flashsale
from api.serializers import BookSer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from api.filters import ProductFilter
from django_filters import rest_framework as django_filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
class CustomPagination(PageNumberPagination):
    page_size = 5

class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    pagination_class = CustomPagination
    queryset = Book.objects.all()
    serializer_class = BookSer

    filter_backends = (filters.SearchFilter,django_filters.DjangoFilterBackend)
    search_fields = ["title","description"]
    filterset_class = ProductFilter

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        related_books = Book.objects.filter(genre=instance.genre).exclude(id=instance.id)

        related_serializer = BookSer(related_books,many=True)
        return Response({
            'book':serializer.data,
            'related_books':related_serializer.data,
        })
    @action(detail=True,methods=["GET"])
    def average_rating(self,request,pk=None):
        book = self.get_object()
        reviews = book.reviews.all()

        if reviews.count()==0:
            return Response({"message":"There is no reviews yet("})

        return Response({"average_rating":sum([review.rating for review in reviews])/reviews.count()})
