from django.urls import path,include
from api.views import *
from rest_framework.routers import DefaultRouter
from .services import replanish_stock
from . import signals
from sms_auth.views import SMSAuthenticationViewSet
from billing.views import CreateChargeView




router = DefaultRouter()
router.register(r"book",ProductViewSet)
router.register(r"order",OrderViewSet,"order")
router.register(r"review",ReviewViewSet,"review")
router.register(r"author",AuthorViewSet,"author")
router.register(r"genre",GenreViewSet,"genre")
router.register(r"flashsale",FlashSaleViewSet,"flashsale")


urlpatterns = [
    path("v1/",include(router.urls)),
    path('v1/auth/',include("djoser.urls")),
    path('v1/admin/replanish_stock/<int:book_id>/<int:amount>',replanish_stock,name="replanish_stock"),
    path('v1/billing/',CreateChargeView.as_view(),name="pay"),
    path('v1/sms_auth/send_sms/',SMSAuthenticationViewSet.as_view({"post":"send_sms"})),
    path('v1/sms_auth/verify_sms/',SMSAuthenticationViewSet.as_view({"post":"verify_sms"})),

]