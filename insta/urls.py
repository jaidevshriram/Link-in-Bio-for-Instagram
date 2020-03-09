from django.urls import path

from . import views

app_name = 'insta'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('create-post/', views.create_post, name='create_post'),
]