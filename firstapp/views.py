from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
@api_view()
@permission_classes((AllowAny, ))
def first(request):
    return Response({'message': 'we received your request'})