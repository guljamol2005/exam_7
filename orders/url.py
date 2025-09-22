from django.urls import path
from .views import OrderListCreateView, OrderDetailView, AdminOrderListView

urlpatterns = [
    path("orders/", OrderListCreateView.as_view(), name="order-list-create"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("orders/admin/", AdminOrderListView.as_view(), name="order-admin-list"),
]
