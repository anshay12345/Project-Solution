from django.shortcuts import render

# Create your views here.
from . import serializers
from . import models
from . import permissions
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HelloApiView(APIView):
    #  FOR TEST API VIEW

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        # RETURNS A LIST OF APIVIEW FEATURES

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        # FOR GENERATING A Hello MESSAGE WITH OUR NAME.

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        # FOR HANDLING UPDATING AN OBJECT

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        # PATCHES REQUEST, ONLY UPDATE FIELDS PROVIDED IN THE REQUEST.

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        # DELETE AN OBJECT

        return Response({'method': 'delete'})
