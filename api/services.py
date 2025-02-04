from api.models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from api.models import Flashsale
from django.core.exceptions import ObjectDoesNotExist

@api_view(http_method_names=["post"])
def replanish_stock(request,book_id,amount):
    try:
        book = Book.objects.get(pk=book_id)
        book.increase_stock(amount)
        book.save()
        return Response({"succes":f"Now stock increased to {book.stock}"})
    except:
        return Response({"error":"Something went wrong :/"},status=400)

def get_active_sale(product_id):
    try:
        sale = Flashsale.objects.get(book__id=product_id) #instance needed
        if not sale:
            return False
        return sale if sale.start_time <= timezone.now() <=sale.end_time else False
    except ObjectDoesNotExist:
        return False
def calculate_total_price(order):
    total_price = order.product.price * order.quantity
    active_sale_for_product = get_active_sale(product_id=order.product.id)
    if active_sale_for_product:
        total_price = total_price-((total_price / 100) * active_sale_for_product.discount_perc)
    return total_price