"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg.generators import OpenAPISchemaGenerator
from django.conf import settings

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
        title="E-Book shop API",
        default_version='v1',
        description="API documentation for Online Book shop",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="husniyor09@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=JWTSchemaGenerator,
)
if settings.ENVIRONMENT=="product":
    schema_view = get_schema_view(
        openapi.Info(
            title="E-Book shop API",
            default_version='v1',
            description="API documentation for Online Book shop",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="husniyor09@gmail.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
        generator_class=JWTSchemaGenerator,
        url='https://api.azimboyev.uz/api/v1'
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path("ai/",include("aiagent.urls")),
    path("api/",include("api.urls")),
    # path("api/v1/sms_auth/",include("sms_auth.urls")),

    # swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
