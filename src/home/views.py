from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SignUpForm, ContactForm
from .models import SignUp
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.conf.urls.static import static

# Create your views here.
def home(request):
	title = "Sign Up Now"
	# if request.user.is_authenticated():
	# 	title += " %s" %(request.user)

	context = {
		"title": title,
	}

	# if request.method == "POST":
	# 	print (request.POST)

	if request.user.is_authenticated() and request.user.is_staff:
		#print (SignUp.objects.all())
		
		# for instance in SignUp.objects.all():
		# 	print(instance)
		# 	print(instance.full_name)

		# queryset = SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains="BK")
		# queryset = SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="BK")
		queryset = SignUp.objects.all().order_by('-timestamp')
		print (SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="BK").count())
		context = {
			"queryset": queryset
		}

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