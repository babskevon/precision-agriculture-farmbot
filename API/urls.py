from django.contrib import admin
from django.urls import path, include
from API.views import TestView, IndexView, Login,ImageUpload,Signout, Photos, Irrigate

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('data/', TestView.as_view(),name='datas'),
    path('login/', Login.as_view(), name='login'),
    path('photo/',ImageUpload.as_view(), name='photo'),
    path('logout/', Signout.as_view(),name='logout'),
    path('garden/',Photos.as_view(),name='photos'),
    path('irrigate/',Irrigate.as_view(), name='irrigate'),
]