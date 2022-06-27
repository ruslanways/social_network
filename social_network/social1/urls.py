from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='social1_index'),
    path('<name>/', views.name, name='name'),
]
