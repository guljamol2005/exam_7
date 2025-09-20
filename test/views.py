from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from .models import BlogPost, Category
from .serializers import BlogPostSerializer, CategorySerializer
from .utils.custom_response import CustomResponse


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        blogs = self.get_queryset()
        serializer = self.serializer_class(blogs, many=True)
        return CustomResponse.success(
            message_key='SUCCESS',
            request=request,
            data=serializer.data,
            name="Guljamol"
        )


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category
    serializer_class = CategorySerializer