from django.conf.urls import url
# from django.contrib import admin
from . import views

# def index(request):
#     print ("Hello")

urlpatterns = [

    url(r'^$', views.index),
    url(r'^results$',views.results),
    url(r'^surveys/process$',views.process)
]
