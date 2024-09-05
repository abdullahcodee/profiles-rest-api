from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


from .import serializers
from rest_framework import status

"""define hello API view """

class HelloAPIView(APIView):

    serializer_class = serializers.HelloSerialzer

    def get(self,request, format=None):
        """return a list of APIview features"""
        an_api_view = [
            'Usese HTTP methods as functions (get, POST, Patch, Put, Delete)',
            'it is  Similar to traditional Django View',
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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """handles updating objects"""

        return Response({'method':'put'})
    def patch(self,request,pk=None):
        """patch only updating the fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request):
        """delete is for deleting an object"""

        return Response({'method':'delete'})


