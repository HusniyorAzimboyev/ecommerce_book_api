from api.models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(http_method_names=["post"])
def replanish_stock(request,book_id,amount):
    try:
        book = Book.objects.get(pk=book_id)
        book.increase_stock(amount)
        book.save()
        return Response({"succes":f"Now stock increased to {book.stock}"})
    except:
        return Response({"error":"Something went wrong :/"},status=400)