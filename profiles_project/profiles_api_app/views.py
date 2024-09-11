from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


from .import serializers
from .import models
from .import permissions


from rest_framework import filters

#read the differnece between APIVIew and ViewSets in the urls.py comment

"""define hello API view """

class HelloAPIView(APIView):

    serializer_class = serializers.HelloSerialzer

    def get(self,request, format=None):
        """return a list of APIview features"""
        an_api_view = [
            'Usese HTTP methods as functions (get, POST, Patch, Put, Delete)',
            'it is Similar to traditional Django View',
            'Gives you the most control over your logic',
            'Is Mapped manually to URLs'
            ]
        return Response({
        'message': 'hello',
        'an_API_view': an_api_view
        })

    def post(self,request):
        serializer = serializers.HelloSerialzer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "hello {0}".format(name)

            return Response({
            'message':message
            })

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
     """handles updating objects"""
     return Response({'method':'put'})

    def patch(self,request,pk=None):
        """patch only updating the fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """delete is for deleting an object"""

        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """return a hello message"""

    """we are using th same serializer here """
    serializer_class = serializers.HelloSerialzer

    def list(self,request):
        a_viewSet = [
            "uses actions (list, create, update retrive, partial_update)",
            "Automatically maps to URLs using routers",
            "Provides more fanctionality with less code"
        ]

        return Response({
            "message": "hello",
            "a_view_set": a_viewSet
        })

    def create(self, request):
        """create a new hello message"""

        serializer = serializers.HelloSerialzer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get("name")
            message = "Hello {0}".format(name)

            return Response({
                "message":message
            })

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Handle getting an object by it's ID"""

        return Response({'http_method': 'GET'})

    def update(self,request,pk=None):
        """Handles updating an object with ID"""

        return Response({'http_method': 'PUT'})

    def partial_update(self,request,pk=None):

        """Handles updating specific part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self,request,pk=None):
        """Handles Deleting an object"""

        return Response({'http_method': 'DELETE'})

class UserProfileViewset(viewsets.ModelViewSet):
    """ModelViewSet is specialized to handle create , update, delete,retrive, and destroy while handling APIs through models"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name','email', )


