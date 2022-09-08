from django.urls import path
from apps.order import views

urlpatterns = [
    path('login/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
]