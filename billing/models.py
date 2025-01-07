from django.db import models
from api.models import Order

class Bill(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=False)
    stripe_charge_id = models.CharField(max_length=60)
    amount = models.DecimalField(decimal_places=2,max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
