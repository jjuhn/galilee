"""GalileeChurchWeb URL Configuration

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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # my own pages
    url(r'^$', 'home.views.home', name='home'),
    
    url(r'^mission/$', 'home.views.welcome', name='welcome'),
    url(r'^mission/$', 'home.views.mission', name='mission'),
    url(r'^about/$', 'home.views.about', name='about'),
    url(r'^staff/$', 'home.views.staff', name='staff'),
    url(r'^location/$', 'home.views.location', name='location'),
    url(r'^contact/$', 'home.views.contact', name='contact'),



    url(r'^ministries/$', 'home.views.ministries', name='ministries'),
    url(r'^ministries/ministry$', 'home.views.ministry', name='ministry'),
    url(r'^ministries/finance$', 'home.views.finance', name='finance'), # 
    url(r'^ministries/worship$', 'home.views.worship', name='worship'), # 
    url(r'^ministries/rearing$', 'home.views.rearing', name='rearing'), # 



    url(r'^community/$', 'home.views.community', name='community'),
    url(r'^community/awana$', 'home.views.awana', name='awana'),
    url(r'^community/gaddiel$', 'home.views.gaddiel', name='gaddiel'),
    url(r'^community/joys$', 'home.views.joys', name='joys'),
    url(r'^community/withim$', 'home.views.withim', name='withim'),
    url(r'^community/adult$', 'home.views.adult', name='adult'),

    url(r'^media/$', 'home.views.media', name='media'),
    url(r'^media/photo/$', 'home.views.photo', name='photo'),
    url(r'^media/video/$', 'home.views.video', name='video'),

    url(r'^news/$', 'home.views.news', name='news'),

    # not using
    # url(r'^$', 'home.views.contact', name='contact'), 
]
