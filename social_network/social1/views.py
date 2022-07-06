from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework import generics
from django.contrib.auth.models import User
from .forms import LoginUserForm
from .serializers import UserSerializer

def name(request, name):
    if name == 'Russia':
        raise Http404('Fuck Russia')
    return render(request,'name.html', {'name': name})

class UsersAPIView(generics.ListAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer


def index(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                form.save()
                return HttpResponseRedirect(reverse('name', args=(form.cleaned_data['username'],)))
            except:
                form.add_error(None, 'Error addition user')
    else:
        form = LoginUserForm()
    return render(request, 'social1/form.html', {'form': form})
