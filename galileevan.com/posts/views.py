from django.shortcuts import render

from posts.models import Post

# Create your views here.
# def posts_home(request):
# 	queryset = Post.objects.all().order_by('-timestamp')
# 	context = {
# 		"object_list": queryset,
# 		"title": "Galilee News"

# 	}
# 	return render(request, "posts.html", context)	


def posts_create(request):
	context = {

	}
	return render(request, "posts.html", context)

def posts_detail(request):
	context = {
	
	}
	return render(request, "posts.html", context)

def posts_list(request):
	context = {
	
	}
	return render(request, "posts.html", context)	

def posts_update(request):
	context = {
	
	}
	return render(request, "posts.html", context)

def posts_delete(request):
	context = {
	
	}
	return render(request, "posts.html", context)	