from django.shortcuts import render

# Create your views here.
# Product endpoints:
# /products/ -> GET: AllowAny, POST: IsAuthenticated + IsAdmin (faqat admin mahsulot qo'sha oladi)
# /products/<id>/ -> GET: AllowAny, PUT/PATCH/DELETE: IsAuthenticated + IsAdmin

from rest_framework.decorators import api_view, permission_classes
from .models import Product, Category
from . serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

@api_view(["GET", "POST"])
def product_index(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        if request.user.is_authenticated and request.user.is_staff:
            serializer = ProductSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(
                {"detail": "Admin permission required"},
                status=status.HTTP_403_FORBIDDEN
            )
    
@api_view([ "GET" ,"PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated, IsAdminUser])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"Message": "Object does not exists"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(
                {"Message": "Something went wrong"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    elif request.method == "PATCH":
        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(
                {"Message": "Something went wrong"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    





@api_view(["GET", "POST"])
def category_index(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        if request.user.is_authenticated and request.user.is_staff:
            serializer = CategorySerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(
                {"detail": "Admin permission required"},
                status=status.HTTP_403_FORBIDDEN
            )
    
@api_view([ "GET" ,"PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated, IsAdminUser])
def category_detail(request, pk):
    try:
         category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"Message": "Object does not exists"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(
                {"Message": "Something went wrong"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    elif request.method == "PATCH":
        serializer = CategorySerializer(instance=category, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(
                {"Message": "Something went wrong"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
