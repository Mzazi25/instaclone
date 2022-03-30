from django.conf.urls import url
from django.urls import re_path,include
from . import views

urlpatterns=[
    re_path(r'^accounts/', include('django_registration.backends.one_step.urls')),
    
    ]