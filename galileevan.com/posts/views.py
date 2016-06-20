from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


from posts.models import Post
from .forms import PostForm

# Create your views here.
# def posts_home(request):
# 	queryset = Post.objects.all().order_by('-timestamp')
# 	context = {
# 		"object_list": queryset,
# 		"title": "Galilee News"

# 	}
# 	return render(request, "posts.html", context)	


def posts_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created!")
		return HttpResponseRedirect(instance.get_absolute_url())

	# if request.method == "POST":
	# 	print (request.POST.get("content"))
	# 	print (request.POST.get("title"))
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def posts_detail(request, id):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

def posts_list(request):
	queryset_list = Post.objects.all().order_by("-timestamp")
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page_request_var = "abc"
	page = request.GET.get(page_request_var)
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	
	context = {
		"object_list": queryset,
		"title": "List",
		"page_request_var": page_request_var,
	}	

	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "logged in"
	# 	}
	# else:
	# 	context = {
	# 		"title": "who are you?"
	# 	}
	return render(request, "post_lists.html", context)	







def posts_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		print (form.cleaned_data.get("title"))
		instance.save()
		# message success
		messages.success(request, "Saved!")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)

def posts_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("posts:list")



