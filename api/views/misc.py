from api.models import Review,Genre,Author,Flashsale,Order
from rest_framework import viewsets,generics
from api.permissions import IsStaff,IsOwner
from api.serializers import *
from rest_framework.permissions import IsAuthenticated
class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSer


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSer

class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSer

class FlashSaleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaff]
    queryset = Flashsale.objects.all()
    serializer_class = FlashSaleSer