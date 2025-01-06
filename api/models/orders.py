from django.db import models
from .objects import Book
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Please enter Uzbek number in format +998XXXXXXXXX"
)

class Order(models.Model):
    PENDING = "Pending"
    PROCESSING = "Processing"
    SHIPPED = "Shipping"
    DELIVERED = "Delivered"
    CANCELED = "Canceled"

    customer = models.CharField(max_length=100)
    product_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    phone_number = models.CharField(max_length=20,validators=[phone_regex])
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,
                              choices=(
                                  (PENDING,"Pending"),
                                  (PROCESSING,"Processing"),
                                  (SHIPPED,"Shipping"),
                                  (DELIVERED,"Delivered"),
                                  (CANCELED,"Canceled")
                              ))
    is_paid = models.BooleanField(default=False,blank=True,null=True)


    def set_status(self,new_status):
        allowed = {
            self.PENDING: [self.PROCESSING, self.CANCELED],
            self.PROCESSING: [self.SHIPPED, self.CANCELED],
            self.SHIPPED: [self.DELIVERED, self.CANCELED]
        }
        if new_status in self.status and self.status in allowed.get(self.status):
            self.status = new_status
            self.save()

        return "Invalid status"