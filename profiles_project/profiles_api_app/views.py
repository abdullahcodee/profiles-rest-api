from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
"""this 2 to handle the login request we create view and passes the request through obtain Auth Token  """
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
"""it give the user the permission to do anything if they are authinticated and prevent them from doing anythin if they are not authinticated"""
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated


from .import serializers
from .import models
from .import permissions


from rest_framework import filters

#read the differnece between APIVIew and ViewSets in the urls.py comment

for user in models.UserProfile.objects.all():
    Token.objects.get_or_create(user=user)

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



class LoginViewSet(viewsets.ViewSet):
    """ checks email and password and returns an Auth token """
    serializer_class = AuthTokenSerializer

    def create(self,request):
        """use ObtainAuthToken AOIView to validate and create a Token"""
        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handels creating, reading, and updating profile feed Items """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus,IsAuthenticated)


    def perform_create(self, serializer):
        """set the user profile to the logged in user """
        serializer.save(user_profile= self.request.user)
        """ensures feed items are associated with the correct user."""








