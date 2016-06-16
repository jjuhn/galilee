from django import forms
from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()



class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email' ]

	def clean_email(self):
		# self.cleaned_data: do self validation that django provides
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		# print ("extention is: ", extension)
		

		# if not extension == "edu":
		# 	raise forms.ValidationError("Please use a valid .edu email adderss.")
		
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		# write validation code 
		return full_name 