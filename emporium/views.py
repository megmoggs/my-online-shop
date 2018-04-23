from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from emporium.forms import PostForm


def product_listing(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'emporium/product_listing.html', {'posts':posts})

def post_new(request):
    form = PostForm()
    return render(request, 'emporium/post_edit.html', {'form':form})

