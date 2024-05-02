from django.urls import path
from .views import exchange_rate

urlpatterns = [
    path('rate/', exchange_rate)
]
