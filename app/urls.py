from django.urls import path
from .views import index, register, add_cashflow, cashflow_detail, cashflow_edit

urlpatterns = [
    path('', index, name='index'),
    path('accounts/register/', register, name='register'),
    path('add/', add_cashflow, name='add_cashflow'),
    path('cashflow/<int:pk>/', cashflow_detail, name='cashflow_detail'),
    path('cashflow/<int:pk>/edit/', cashflow_edit, name='cashflow_edit'),
]