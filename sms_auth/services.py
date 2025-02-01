from .serializers import SMSSerializer
from django.conf import settings
import random
import requests

SMS_KEY = settings.SMS_KEY
def send_sms_via_infobip(serializer):
    phone_number = serializer.validated_data["phone_number"]

    verification_code = str(random.randint(100000, 999999))
    print(verification_code)

    # Send SMS via Infobip
    url = f'https://{settings.SMS_BASE_URL}/sms/2/text/advanced'
    headers = {
        'Authorization': f'App {SMS_KEY}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'

    }

    payload = {
    "messages": [
        {
            "destinations": [{"to":phone_number}],
            "from": "Book_ecommerce_Hugo",
            "text": f"your verification code is {verification_code}"
        }
    ]
}
    response = requests.post(url, json=payload, headers=headers)
    return {"response":response,"phone_number":phone_number,"verification_code":verification_code}
