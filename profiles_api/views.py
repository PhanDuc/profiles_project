from django.shortcuts import render
# Import two Object tromg rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# Inherit from APIVIEW
class HelloApiView(APIView):
    """Test API View."""
    def get(self, resquest, format=None):
        """Return a list of APIView features."""
        an_apiview = [
            'Users HTTP methods as function : get, post, patch, put, delete',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'It mapped manually to URLS'
        ]

        # Response as dictionary
        return Response({'message':'Hello', 'an_apiview':an_apiview})

