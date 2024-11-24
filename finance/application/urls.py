"""
URL configuration for finance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from application.views import home, signup, user, signup_save, add_entry, user_tab, delete_transaction

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('save/', user, name='user'),
    path('signup_save/', signup_save, name='signup_save'),
    path('add_entry/', add_entry, name='add_entry'),
    path('user_tab/', user_tab, name='user_tab'),
    path('admin/', admin.site.urls),
    path('delete_transaction/', delete_transaction, name='delete_transaction'),
    path('user_tab/', user_tab, name='user_tab'),
    
]




