import os, sys
if sys.platform.startswith('linux'): # python 2.x
	from urllib import quote_plus
else:
	from urllib.parse import quote_plus # python 3.x


from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from django.views.generic.edit import FormView
from posts.models import Post
from .forms import PostForm, UploadFileForm

from .models import upload_location
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render



def handle_uploaded_file(f):
	with open(r'c:\etc\temp.txt' + str(count), 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)


def upload_file(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect(instance.get_absolute_url())
	else:
		form = UploadFileForm()
	return render(request, 'post_form.html', {'form': form})





def posts_create(request):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	# if not request.user.is_authenticated():
	# 	raise Http404



	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		
		for count, x in enumerate(request.FILES.getlist("files")):
			def process(f):
			    with open(r'c:\etc\temp.txt' + str(count), 'wb+') as destination:
			        for chunk in f.chunks():
			            destination.write(chunk)
			process(x)

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
	share_string = quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "post_detail.html", context)

def posts_list(request):
	today = timezone.now().date()

	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all().order_by("-timestamp")
	else:
		queryset_list = Post.objects.filter(user=request.user)
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(user__first_name__icontains=query) |
			Q(user__last_name__icontains=query)
		).distinct()

	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page_request_var = "page"
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
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
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
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("posts:list")



