from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from PIL import Image
#from .imageresize import *

# Create your models here.
def generate_slug(s):
	new_slug=slugify(s, allow_unicode=True)
	return new_slug+'-'+str(int(timezone.now().timestamp()))

def generate_image_path(instance, filename):
	time_now=timezone.now()
	slug = instance.post.slug
	image_upload_path = '/'.join(['post_images',str(time_now.year),str(time_now.month),str(time_now.day),str(slug),str(filename)])
	return image_upload_path

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length = 100)
	text = models.TextField()
	slug = models.SlugField(max_length=150, blank=True)
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'slug':self.slug})

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug=generate_slug(self.title)
		super().save(*args,**kwargs)

class Gallery(models.Model):
	post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='gallery')
	image = models.ImageField(upload_to=generate_image_path, null=True, blank=True)

	def save(self, *args, **kwargs):
		super(Gallery, self).save()
		image = Image.open(self.image.path)
		(width, height) = image.size
		if width<=800:
			factor = 1
		else:
			factor = width/height
			width = 800
			height = width/factor
		print(factor)
		size = (int(width), int(height))
		print(size)
		image = image.resize(size, Image.ANTIALIAS)
		print(self.image.path)
		print(image.size)
		image.save(self.image.path)

#	def save(self, *args, **kwargs):

