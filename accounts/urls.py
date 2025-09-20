from django.urls import path
from .views import RegisterCreateAPIView, LoginAPIView, TokenRefreshView, ProfilAPIView


urlpatterns = [
    path('register/', RegisterCreateAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('profil/', ProfilAPIView.as_view()),
]