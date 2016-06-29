from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.mail import send_mail
from .models import SignUp
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.conf.urls.static import static

from news.models import Post



def event(request):
	title = "Event"
	context = {
		"title": title,
	}
	return render(request, "event.html", context) 

def user_settings(request):
	form = SignUpForm(request.POST or None)
	context = {
		"form": form,
	}	

	# if request.method == "POST":
	# 	print (request.POST)
	print (request.user)

	user = User.objects.get(username=request.user)
	if form.is_valid() and request.method == "POST":  # go through whole validation in forms.py 
		#instance = form.save(commit=False)
		
		user.first_name = form.cleaned_data.get("first_name")
		user.last_name = form.cleaned_data.get("last_name")
		user.save()
		message = "Your information is saved."
		context = {
			"form": form,
			"message": message,
		}

	

	return render(request, "user_settings.html", context) 

# Create your views here.
def home(request):
	title = "Sign Up Now"
	# if request.user.is_authenticated():
	# 	title += " %s" %(request.user)
	latest_post = Post.objects.latest('timestamp')
	context = {
		"recent_post" : latest_post,
		"title": title,
	}

	# if request.method == "POST":
	# 	print (request.POST)

	# if request.user.is_authenticated() and request.user.is_staff:
	# 	print (SignUp.objects.all())
		
	# 	for instance in SignUp.objects.all():
	# 		print(instance)
	# 		print(instance.full_name)

	# 	queryset = SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains="BK")
	# 	queryset = SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="BK")
	# 	queryset = SignUp.objects.all().order_by('-timestamp')
	# 	print (SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="BK").count())
	# 	context = {
	# 		"queryset": queryset
	# 	}

	return render(request, "home.html", context) # {} is context


def welcome(request):
	return render(request, "welcome_mission.html", {})
def mission(request):
	return render(request, "welcome_mission.html", {})
def about(request):
	return render(request, "welcome_about.html", {})
def staff(request):
	return render(request, "welcome_staff.html", {})
def location(request):
	return render(request, "welcome_location.html", {})
def contact(request):
	return render(request, "welcome_contact.html", {})


def ministries(request):
	return render(request, "mini_ministry.html", {})
def ministry(request):
	explaination = "nothing"


	context = {
		"explaination": explaination
	}
	return render(request, "mini_ministry.html", context)
def finance(request):
	return render(request, "mini_finance.html", {})
def worship(request):
	return render(request, "mini_worship.html", {})
def rearing(request):
	return render(request, "mini_rearing.html", {})


def community(request):
	return render(request, "comm_awana.html", {})
def awana(request):
	return render(request, "comm_awana.html", {})
def gaddiel(request):
	return render(request, "comm_gaddiel.html", {})
def joys(request):
	return render(request, "comm_joys.html", {})
def withim(request):
	return render(request, "comm_withim.html", {})
def adult(request):
	return render(request, "comm_adult.html", {})


def media(request):
	return render(request, "media_photo.html", {})
def photo(request):
	return render(request, "media_photo.html", {})
def video(request):
	return render(request, "media_video.html", {})


# def login(request):
# 	return render(request, "login.html", {})

# def register(request):
# 	return render(request, "register.html", {})	

# def pwd_reset(request):
# 	return render(request, "pwd_reset.html", {})		

# def news(request):
# 	return render(request, "news.html", {})	


# this is not using a model form, so we cannot save data
# def contact(request):
# 	title = 'Contact Us'
# 	title_align_center = True
# 	form = ContactForm(request.POST or None)

# 	if form.is_valid():
# 		# iterate all field
# 		# for key in form.cleaned_data:
# 		# 	#print (key)
# 		# 	print (form.cleaned_data.get(key))

# 		form_email = form.cleaned_data.get("email")
# 		form_message = form.cleaned_data.get("message")
# 		form_full_name = form.cleaned_data.get("full_name")
# 		# print (email, message, full_name)

# 		subject = 'Site contact form'
# 		from_email = settings.EMAIL_HOST_USER
# 		to_email = [from_email, 'benjamin3726@gmail.com']
# 		contact_message = "%s: %s via %s"%(
# 			form_full_name, 
# 			form_message, 
# 			form_email)

# 		send_mail(subject, contact_message, from_email,
#     to_email, fail_silently=True)

# 	context = {
# 		"form": form,
# 		"title": title,
# 		"title_align_center": title_align_center,
# 	}

# 	return render(request, "form.html", context)


def save_image(request):
	if request.POST:
		# save it somewhere
		f = open(settings.MEDIA_ROOT + '/webcamimages/someimage.jpg', 'wb')
		f.write(request.raw_post_data)
		f.close()
		# return the URL
		return HttpResponse('http://localhost:8080/site_media/webcamimages/someimage.jpg')
	else:
		return HttpResponse('no data')