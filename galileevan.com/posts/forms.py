from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	# file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"image",
			"image2",
			"image3",
			"image4",
			"image5",
			# "draft",
			# "publish",
		]


class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.FileField()