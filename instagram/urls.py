"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import gram
from django.contrib import admin
from django.urls import include, re_path
from django.contrib.auth import views
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LoginView,LogoutView 


urlpatterns = [

    re_path(r'^admin/', admin.site.urls),
    re_path(r'',include('gram.urls')),
    re_path('accounts/register/',
        RegistrationView.as_view(success_url='/account/'),
        name='django_registration_register'),
    re_path(r'^accounts/', include('django_registration.backends.one_step.urls')),
    re_path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^logout/$', LogoutView.as_view, {"next_page": '/'}),
    re_path(r'^login/$', LoginView.as_view(), {"next_page": '/'}),
]
