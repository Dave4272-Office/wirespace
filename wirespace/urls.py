"""wirespace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin
from share.views import authenticate,editor_authenticate,editor

urlpatterns = [
	#url(r'^(?P<k>[a-z0-9]+)/$',authenticate,name='authenticate'),
    url(r'^auth/(?P<k>[a-z0-9]+)/$',authenticate,name='authenticate'),
    url(r'^editor/(?P<k>[a-f0-9]{16})[/]?$',editor_authenticate,name='editor_authenticate'),
	url(r'^editor[/]?',editor,name='editor'),
    url(r'^',include('share.urls')),
    url(r'^share/',include('share.urls')),
    url(r'^host/', admin.site.urls),
]

