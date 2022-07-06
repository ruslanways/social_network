from django.views.generic import ListView, DetailView
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework import generics
from django.contrib.auth.models import User
from .forms import FileUploadForm, LoginUserForm
from .serializers import UserSerializer
from .models import Post
from django.views.generic.edit import CreateView

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


def handle_uploaded_file(f):
    with open('social1/newfile', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse('name', args=(f"File '{form.cleaned_data['title']}' uploaded",)))
    else:
        form = FileUploadForm()
    return render(request, 'social1/upload.html', {'form': form})


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/'
