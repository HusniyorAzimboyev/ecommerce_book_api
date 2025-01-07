import datetime

from rest_framework.serializers import ModelSerializer,SerializerMethodField,ValidationError
from api.models import Order,Book
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
class OrderSer(ModelSerializer):
    total_price = SerializerMethodField()
    def get_total_price(self,obj):
        return obj.product.price * obj.quantity

    class Meta:
        model = Order
        fields = ["id","customer","product","quantity","phone_number","created_at","status","is_paid","total_price"]

    def validate_quantity(self,value):
        try:
            product_id = self.initial_data["product"]
            product = Book.objects.get(id=product_id)
            if value>product.stock:
                raise ValidationError("There is not enough items in stock!")
            if value<1:
                raise ValidationError("Quantity must be at least 1!")
            return value
        except ObjectDoesNotExist:
            raise ValidationError("Product doesn't exist!")

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)

        product = order.product
        product.stock -= order.quantity
        product.save()
        return order

