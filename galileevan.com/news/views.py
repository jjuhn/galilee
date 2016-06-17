from django.http import HttpResponse
from django.shortcuts import render

from news.models import Post
from datetime import datetime, timedelta

# Create your views here.
def posts_home(request):
	queryset = Post.objects.all().order_by('-timestamp')
	context = {
		"object_list": queryset,
		"title": "Galilee News"

	}
	return render(request, "news.html", context)	

	
