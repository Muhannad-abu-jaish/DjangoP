from django.shortcuts import render , get_object_or_404
from .models import Post
from django.http import Http404

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

#Display all the posts
def post_list(request):
    posts = Post.objects.all()
    #render its for rendreing a page
    return render(request, 'blog/post/list.html', {'posts': posts})

#Display one specific post
def post_detail(request, id):
    #this function if this specific post does not exsits
    #it will return a 404 error page
    post = get_object_or_404(Post, id = id, status = Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post' : post})