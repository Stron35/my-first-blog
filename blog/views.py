from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Post, Gallery
from .forms import PostForm

# Create your views here.

def post_list(request):
	posts = Post.objects.all().order_by('-published_date')
	return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug__iexact = slug)
	return render(request, 'blog/post_detail.html', {'post':post})

class PostCreate(CreateView):
	model = Post
	fields = ['title', 'text',]

	def form_valid(self, form):
		new_post = form.save(commit = False)
		new_post.author = self.request.user
		new_post.published_date = timezone.now()
		new_post.save()
		print(self.request.FILES.getlist('gallery'))
		for item in self.request.FILES.getlist('gallery'):
			Gallery.objects.create(image = item, post = new_post)	
		return super().form_valid(form)

	def get(self, request):
		form = PostForm()
		return render(request, 'blog/post_edit.html', {'form': form})

class PostEdit(UpdateView):
	model = Post
	fields = ['title', 'text',]

	def get(self, request,  *args, **kwagrs):
		self.post = get_object_or_404(Post, slug__iexact = kwagrs['slug'])
		self.form = PostForm(instance = self.post)
		return render(request, 'blog/post_edit.html', {'form': self.form, 'post':self.post})

	def form_valid(self, form):
		edit_post = form.save(commit=False)
		edit_post.author = self.request.user
		edit_post.save()
		for item in self.request.FILES.getlist('gallery'):
			Gallery.objects.create(image = item, post = edit_post)	
		return super().form_valid(form)

class PostDelete(View):
	def get(self, request,  slug):
		self.post = Post.objects.get(slug__iexact = slug)
		self.form = PostForm(instance = self.post)
		return render(request, 'blog/post_delete.html', {'form': self.form, 'post':self.post})

	def post(self, request, slug):
		post = Post.objects.get(slug__iexact = slug)
		post.delete()
		return redirect(reverse('post_list'))


def access_denied(request):
	return render(request, 'blog/access_denied.html', message)