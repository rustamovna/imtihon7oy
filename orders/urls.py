from django.urls import path
from .views import (
    CreateOrderView, OrderListView, OrderDetailView, UpdateOrderStatusView, CancelOrderView
)

urlpatterns = [
    path('orders/create/', CreateOrderView.as_view()),
    path('orders/', OrderListView.as_view()),
    path('orders/<int:pk>/', OrderDetailView.as_view()),
    path('orders/<int:pk>/status/', UpdateOrderStatusView.as_view()),
    path('orders/<int:pk>/cancel/', CancelOrderView.as_view()),
]
