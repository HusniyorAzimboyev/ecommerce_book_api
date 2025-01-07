from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from api.models import Order
from config.settings import TELEGRAM_BOT_TOKEN,ADMIN_ID

@receiver(post_save,sender=Order)
def notify_admin(sender,instance,created,**kwargs):
    if created:
        token = TELEGRAM_BOT_TOKEN
        method = "sendMessage"
        message_text = f"New Order: {instance.id}\nBook: {instance.product.title}\nQuantity: {instance.quantity}\nClient: {instance.customer}\nTel: {instance.phone_number}"
        response = requests.post(url=f"https://api.telegram.org/bot{token}/{method}",
                      data={
                          "chat_id":ADMIN_ID,"text":message_text
                      }).json()
        print("Response from telegram api:",response)
