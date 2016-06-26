from django.db import models

# python manage.py makemigrations  (initialize)
# python manage.py migrate   (run)

# Create your models here.
class SignUp(models.Model):
	#full_name = models.CharField(max_length=40, blank=False, null=True)
	first_name = models.CharField(max_length=40, blank=False, null=True)
	last_name = models.CharField(max_length=40, blank=False, null=True)
	#email = models.EmailField()
	

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)  # once it creates save time
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email

	def __str__(self):  #Python 3.3 __str__
		return self.first_name
