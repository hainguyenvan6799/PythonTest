from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('showBookOfAuthor/', views.showBookOfAuthor, name="showBookOfAuthor"),
    path('getFormLogin/', views.getFormLogin, name="getFormLogin"),
    path('postFormLogin/', views.postFormLogin, name="postFormLogin"),
]