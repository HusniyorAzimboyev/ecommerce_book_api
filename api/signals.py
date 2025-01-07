from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Order
from .tasks import send_tg_message
@receiver(post_save,sender=Order)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        send_tg_message.delay(
            order_id=instance.id,
            product_title=instance.title,
            quantity=instance.quantity,
            customer=instance.customer,
            phone_number=instance.phone_number
        )

