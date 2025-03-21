import requests
from config.settings import TELEGRAM_BOT_TOKEN,ADMIN_ID
from celery import shared_task
from time import sleep
@shared_task
def send_tg_message(order_id, product_title, quantity, customer, phone_number,total_price):
    token = TELEGRAM_BOT_TOKEN
    method = "sendMessage"
    message_text = f"New Order: {order_id}\nBook: {product_title}\nQuantity: {quantity}\nClient: {customer}\nTotal price: {total_price} $\nTel: {phone_number}"
    response = requests.post(url=f"https://api.telegram.org/bot{token}/{method}",
                  data={
                      "chat_id":ADMIN_ID,"text":message_text
                  }).json()