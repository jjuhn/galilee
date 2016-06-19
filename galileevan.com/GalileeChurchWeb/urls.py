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
from django.conf.urls import url, include
from django.contrib import admin

from home.views import (
    home,
    welcome, mission, about, staff, location, contact,
    ministries, ministry, finance, worship, rearing,
    community, awana, gaddiel, joys, withim,adult,
    media, photo, video,
    )

from news.views import (
    posts_home,
    )
#from news import views as news_view
#url(r'^news/$', 'news_view.posts_home', name='news'),


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # posts (mock up)
    url(r'^posts/', include("posts.urls")),
    # my own pages
    url(r'^$', home, name='home'),
    
    url(r'^mission/$', welcome, name='welcome'),
    url(r'^mission/$', mission, name='mission'),
    url(r'^about/$', about, name='about'),
    url(r'^staff/$', staff, name='staff'),
    url(r'^location/$', location, name='location'),
    url(r'^contact/$', contact, name='contact'),



    url(r'^ministries/$', ministries, name='ministries'),
    url(r'^ministries/ministry$', ministry, name='ministry'),
    url(r'^ministries/finance$', finance, name='finance'), # 
    url(r'^ministries/worship$', worship, name='worship'), # 
    url(r'^ministries/rearing$', rearing, name='rearing'), # 



    url(r'^community/$', community, name='community'),
    url(r'^community/awana$', awana, name='awana'),
    url(r'^community/gaddiel$', gaddiel, name='gaddiel'),
    url(r'^community/joys$', joys, name='joys'),
    url(r'^community/withim$', withim, name='withim'),
    url(r'^community/adult$', adult, name='adult'),

    url(r'^media/$', media, name='media'),
    url(r'^media/photo/$', photo, name='photo'),
    url(r'^media/video/$', video, name='video'),

    url(r'^news/$', posts_home, name='news'),


]
