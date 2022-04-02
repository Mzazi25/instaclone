import re
from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.account, name = 'account'),
    re_path(r'^account/',views.account,name='account'),
    re_path(r'^search/', views.search_results, name='search_results')
    
]