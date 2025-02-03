from rest_framework import viewsets,status
from .serializers import SMSSerializer,VerifySMSSerializer
from .services import send_sms_via_infobip
from django.core.cache import cache
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from django.conf import settings

User = get_user_model()

class SMSAuthenticationViewSet(viewsets.ViewSet):
    def send_sms(self,request):
        try:
            serializer = SMSSerializer(data=request.data)
            if serializer.is_valid():
                details = send_sms_via_infobip(serializer)
                if details["response"].status_code == 200:
                    cache.set(serializer.validated_data["phone_number"], details["verification_code"], 1000)
                    def notify_admin_about_log(): #created because of railway doesn't show all logs from service
                        bot_token = settings.TELEGRAM_BOT_TOKEN
                        payload = {
                            "chat_id":"1779062204",
                            "text":f"New login via sms - {details['verification_code']}"
                        }
                        requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage",data=payload)
                    return Response({"message": "SMS sent successfully","data":details["response"].text}, status=status.HTTP_200_OK)
                return Response({"message": "Failed to send SMS"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as error:
            print(error,request.data,serializer.data)
            return Response({"error":f"{Exception}"})

    def verify_sms(self, request):
        serializer = VerifySMSSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = serializer.validated_data['verification_code']
            cached_code = cache.get(phone_number)

            if verification_code == cached_code:
                user, created = User.objects.get_or_create(phone_number=phone_number)
                if created:
                    # Set other fields like username, email, etc. if needed
                    user.save()

                # Generate JWT token for the user
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })

            return Response({"message": "Invalid verification code"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get_cache(self,request):
        code = cache.get("329421")
        cache.clear()
        return(Response({"data":f"{code}"}))


