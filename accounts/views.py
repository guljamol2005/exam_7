from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer
from utils.claim_token import get_tokens_for_user
from rest_framework.response import Response
from rest_framework import status

class RegisterCreateAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]


    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token = get_tokens_for_user(user=user)
            return Response(data=token, status=status.HTTP_200_OK)
        
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class TokenRefreshView(TokenViewBase):
    
    serializer_class = TokenRefreshSerializer


class ProfilAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            "user_id": user.id,
            "username": user.username,
            "password": user.password
        }

        return Response(data = data, status=status.HTTP_202_ACCEPTED)
