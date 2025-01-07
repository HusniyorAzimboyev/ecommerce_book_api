from rest_framework.serializers import ModelSerializer
from api.models import *


class BookSer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


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
