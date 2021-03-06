"""rumahiot_surat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rumahiot_surat.apps.notification.views import email_activation,welcome_email, device_notification_email, forgot_password_email

urlpatterns = [
    url(r'^activation/send$', email_activation, name='email_activation'),
    url(r'^forgot/password/send$', forgot_password_email, name='forgot_password_email'),
    url(r'^welcome/send$', welcome_email, name='welcome_email'),
    url(r'^device/notification/send$', device_notification_email, name='device_notification_email')
]
