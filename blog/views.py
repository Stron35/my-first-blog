from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic.detail import DetailView
from .models import Post
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

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			print(request.FILES)
			if 'images' in request.FILES:
				form.images=request.FILES['images']
			post=form.save(commit=False) #форма всё ещё не сохраняется, дальше добавляется автор и время
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			print(post.slug)
			return redirect('post_detail', slug=post.slug)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug__iexact = slug)
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