from django.urls import path
from .views import dummy,survey_recommendations

urlpatterns = [
    path('1/',dummy),
    path('recommend/',survey_recommendations)
]