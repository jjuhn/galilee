from django.db import models

# python manage.py makemigrations  (initialize)
# python manage.py migrate   (run)

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=40, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)  # once it creates save time
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email

	def __str__(self):  #Python 3.3 __str__
		return self.email
