from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

"""define hello API view """

class HelloAPIView(APIView):
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

