"""jobsphereonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views 
from . import restcontroller

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'job/create/', views.createjob, name='create'),
    url(r'job/jobpostsuccess/', views.jobpostsuccess, name='jobpostsuccess'),
    url(r'job/search/', views.searchjob, name='searchjob'),
    url(r'employer/signup/', views.employersignup, name='employersignup'),
    url(r'employer/signupsuccess/', views.empsignupsuccess, name='empsignupsuccess'),
    url(r'login/', views.userauthentication, name='userauthentication'),
    url(r'logout/', views.dologout, name='dologout'),
    url(r'searchtags/', restcontroller.searchtags, name='searchtags'),
    url(r'gettags/', restcontroller.gettags, name='gettags'),
    url(r'searchlocations/', restcontroller.searchlocations, name='getlocations'),
    url(r'getlocations/', restcontroller.getlocations, name='getlocations'),
    url(r'getcategory/', restcontroller.getcategory, name='getcategory'),
    url(r'postjob/', restcontroller.postjob, name='postjob'),
]
