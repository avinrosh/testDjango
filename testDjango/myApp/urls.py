from django.conf.urls import urls
from myApp import views

urlpatterns=[

url(r'^$', views.index, name='index'),

]
