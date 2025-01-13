from django.urls import path,include,re_path
from api.views import *
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from .services import replanish_stock
from . import signals
from billing.views import CreateChargeView
from drf_yasg.generators import OpenAPISchemaGenerator

class JWTSchemaGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self):
        security_definitions = super().get_security_definitions()
        security_definitions['Bearer'] = {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
        return security_definitions

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation for your project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your.email@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=JWTSchemaGenerator
)


router = DefaultRouter()
router.register(r"book",ProductViewSet)
router.register(r"order",OrderViewSet,"order")
router.register(r"review",ReviewViewSet,"review")
router.register(r"author",AuthorViewSet,"author")
router.register(r"genre",GenreViewSet,"genre")
router.register(r"flashsale",FlashSaleListCreateView,"flashsale")


urlpatterns = [
    path("v1/",include(router.urls)),
    path('v1/admin/replanish_stock/<int:book_id>/<int:amount>',replanish_stock,name="replanish_stock"),
    path('v1/billing/',CreateChargeView.as_view(),name="pay"),

    path('v1/auth/',include("djoser.urls")),

    # swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]