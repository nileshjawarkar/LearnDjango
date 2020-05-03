from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import BookSerializer, BookMiniSerializer
from .models import Book

class BookViewset( viewsets.ModelViewSet ) :
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = ( TokenAuthentication, )
    # permission_classes = (IsAuthenticated)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer( instance )
        return Response( serializer.data )

    def update(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


