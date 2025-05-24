from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('create-blog', views.create_blog, name="create_blog"),
]