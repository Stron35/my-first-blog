from django import forms
#from multiupload.fields import MultiImageField

from .models import Post

class PostForm(forms.ModelForm):
	#image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

	class Meta:
		model=Post
		fields = ('title', 'text', )
	# 	fields = ('image',)

	# def save(self, commit=True):
	# 	images = self.cleaned_data.pop('image')
	# 	instance = super(PostForm, self).save()
	# 	for each in images:
	# 		image = Images(image=each, post=instance)
	# 		image.save()

	# 	return instance


	
    		