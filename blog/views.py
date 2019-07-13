from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from .models import Post, Gallery
from .forms import PostForm

# Create your views here.
# class PostDetailView(DetailView):
# 	model = Post
# 	query_pk_and_slug = True

def post_list(request):
	posts = Post.objects.all().order_by('-published_date')
	print(posts)
	return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug__iexact = slug)
	return render(request, 'blog/post_detail.html', {'post':post})

# def post_new(request):
# 	if request.method == 'POST':
# 		form = PostForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			post = form.save(commit=False) #форма всё ещё не сохраняется, дальше добавляется автор и время
# 			post.author = request.user
# 			post.published_date = timezone.now()			
# 			post.save()
# 			for field in request.FILES.keys():
# 				for formline in request.FILES.getlist(field):
# 					img = Post(images=formline)
# 					print(img)
# 					img.save()
# 			return redirect('post_detail', slug=post.slug)
	# else:
	# 	form = PostForm()
	# 	print('В создании')
	# return render(request, 'blog/post_edit.html', {'form': form})

class PostCreate(CreateView):
	model = Post
	fields = ['title', 'text',]

	def form_valid(self, form):
		print(form)
		new_post = form.save(commit = False)
		new_post.author = self.request.user
		new_post.published_date = timezone.now()
		new_post.save()
		print(self.request.FILES.getlist('gallery'))
		for item in self.request.FILES.getlist('gallery'):
			print(item)
			Gallery.objects.create(image = item, post = new_post)
		
		return super().form_valid(form)
		



	def get(self, request):
		form = PostForm()
		return render(request, 'blog/post_edit.html', {'form': form})
# class PostNew(FormView):
# 	model = Images
# 	template_name = 'blog/post_edit.html'
# 	from_class = PostForm
# 	success_url = reverse_lazy('post_detail:post.slug')
# 	queryset = Images.objects.all()

# 	def form_valid(self, form):
# 		for each in form.cleaned_data['image']:
# 			Images.image.objects.all(image=each)
# 		return super(PostNew, self).form_valid(form)

def post_edit(request, slug):
    post = get_object_or_404(Post, slug__iexact = slug)
    if request.user!=post.author:
    	message='Вы не создатель поста.'
    	print(message)
    	return render(request, 'blog/access_denied.html', {'message':message})
    else:
	    if request.method == "POST":
	        form = PostForm(request.POST,request.FILES, instance=post)
	        if form.is_valid():
	            print(request.FILES['images'])
	            if 'images' in request.FILES:
	                form.images=request.FILES['images']
	            post = form.save(commit=False)
	            post.author = request.user
	            post.published_date = timezone.now()
	            post.save()
	            return redirect('post_detail', slug=post.slug)
	    else:
	        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def access_denied(request):
	return render(request, 'blog/access_denied.html', message)