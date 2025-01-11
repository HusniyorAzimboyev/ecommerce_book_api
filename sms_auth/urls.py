from django.urls import path
from .views import SMSAuthenticationViewSet

urlpatterns = [
    path("send_sms/",SMSAuthenticationViewSet.as_view({'post':'send_sms'})),
    path("verify_sms/",SMSAuthenticationViewSet.as_view({'post':"verify_sms"})),
    path("cache/",SMSAuthenticationViewSet.as_view({"get":"get_cache"}))
]