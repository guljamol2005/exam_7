from django.urls import path

from .views import BlogListCreateAPIView, CategoryCreateAPIView


urlpatterns = [
    path('', BlogListCreateAPIView.as_view()),
    path('category/', CategoryCreateAPIView.as_view()),
]
