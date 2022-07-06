from django.urls import include, path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='social1_index'),
    path('upload/', views.upload_file, name='upload'),
    path('about/', TemplateView.as_view(template_name="social1/about.html")),
    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    path('post_add/', views.PostCreateView.as_view()),
    path('<name>/', views.name, name='name'),
]
