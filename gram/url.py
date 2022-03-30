from django.conf.urls import url
from django.urls import path,include
from . import views

urlpatterns=[
    path('^$',views.welcome,name = 'welcome'),
    path(r'^news/',include('news.urls')),
    path(r'^accounts/', include('django_registration.backends.one_step.urls')),
    
    ]