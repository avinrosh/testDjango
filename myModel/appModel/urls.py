from django.conf.urls import urls
from appModel import views

urlpatterns=[
    url(r'^$',views.index,name='index')

]
