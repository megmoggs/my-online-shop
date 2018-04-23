from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from emporium.forms import PostForm
from django.shortcuts import redirect

def product_listing(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'emporium/product_listing.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'emporium/post_detail.html', {'post':post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save
            return redirect('post_detail.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'emporium/post_edit.html', {'form':form})


