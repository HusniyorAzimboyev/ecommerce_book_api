from rest_framework.serializers import ModelSerializer,SerializerMethodField
from api.models import *
from rest_framework import serializers
from django.utils import timezone

class BookSer(serializers.ModelSerializer):
    active_sale = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'pages', 'description', 'price', 'stock', 'active_sale']

    def get_active_sale(self, obj):
        now = timezone.now()
        flash_sale = Flashsale.objects.filter(book=obj, start_time__lte=now, end_time__gte=now).first()
        return {
            "discount_perc": flash_sale.discount_perc,
            "start_time": flash_sale.start_time,
            "end_time": flash_sale.end_time
        } if flash_sale else None





class GenreSer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ReviewSer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class FlashSaleSer(ModelSerializer):
    class Meta:
        model = Flashsale
        fields = "__all__"


class AuthorSer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
