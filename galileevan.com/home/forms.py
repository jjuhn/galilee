from django import forms
from .models import SignUp



class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['first_name', 'last_name', ] #'email',]
		#fields = ['full_name']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		# write validation code 
		return email

	def clean_first_name(self):
		first_name = self.cleaned_data.get('first_name')
		# write validation code 
		return first_name 

	def clean_last_name(self):
		last_name = self.cleaned_data.get('last_name')
		# write validation code 
		return last_name 