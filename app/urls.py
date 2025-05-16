from django.urls import path
from .views import index, register, add_cashflow

urlpatterns = [
    path('', index, name='index'),
    path('accounts/register/', register, name='register'),
    path('add/', add_cashflow, name='add_cashflow'),
]