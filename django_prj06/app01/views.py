from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

from .serializers import BookSerializer
from .models import Book

class BookViewset( viewsets.ModelViewSet ) :
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = ( TokenAuthentication, )
    # permission_classes = (IsAuthenticated)


