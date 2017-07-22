from django.shortcuts import render
# Import two Object tromg rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

# Create your views here.
# Inherit from APIVIEW
class HelloApiView(APIView):
    """Test API View."""
    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features."""
        an_apiview = [
            'Users HTTP methods as function : get, post, patch, put, delete',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'It mapped manually to URLS'
        ]

        # Response as dictionary
        return Response({'message':'Hello', 'an_apiview':an_apiview})


    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        # Validate data
        if serializer.is_valid():
            # get function
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Updates fields provided in the request"""

        return Response({'method':"patch"})

    def delete(self, request, pk=None):
        """Deletes and object."""
        return Response({'method':'delete'})






