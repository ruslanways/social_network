from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Django.<br>Again.")

def name(request, name):
    if name == 'Russia':
        raise Http404('Fuck Russia')
    return render(request,'name.html', {'name': name})

class UsersAPIView(generics.ListAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
