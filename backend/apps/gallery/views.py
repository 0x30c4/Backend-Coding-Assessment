from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from apps.gallery.serializer import ItemsSerializer
from apps.gallery.models import Items


class ItemsViewList(APIView):
    """
    List all items, or create a new items.
    """

    @swagger_auto_schema()
    def get(self, request, format=None):
        '''
        Returns all the available items.
        '''
        snippets = Items.objects.all()
        serializer = ItemsSerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ItemsSerializer)
    def post(self, request, format=None):
        context = {
            'request': request
        }
        serializer = ItemsSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemsViewDetail(APIView):
    '''
    Retrieve, update or delete a Items instance.
    '''

    def get_object(self, pk):
        '''
        Get object by primary key.
        '''
        try:
            return Items.objects.get(pk=pk)
        except Items.DoesNotExist:
            raise Http404

    def get(self, requests, pk=None, format=None):
        '''
        Get the item by primary key.
        '''
        item = self.get_object(pk)
        serializer = ItemsSerializer(item)
        return Response(serializer.data)

