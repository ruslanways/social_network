from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='social1_index'),
    path('upload/', views.upload_file, name='upload'),
    path('<name>/', views.name, name='name'),
]
