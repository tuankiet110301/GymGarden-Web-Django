from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from hitcount.views import HitCountDetailView
from django.db.models import F
# Create your views here.


def blog(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, "blog.html", {'posts': posts})





def reslug(request, slug):
    blogs = Post.objects.all()
    blog = get_object_or_404(blogs, slug=slug)
    Post.objects.filter(slug=slug).update(views=F('views')+1)
    if blog == blogs.last():
        blog_next1 = blogs.first()
    else:
        blog_next1 = blog.get_previous_by_created_on()
    print(blog_next1)
    if blog_next1 == blogs.last():
        blog_next2 = blogs.first()
    else:
        blog_next2 = blog_next1.get_previous_by_created_on()
    print(blog_next2)
    if blog_next2 == blogs.last():
        blog_next3 = blogs.first()
    else:
        blog_next3 = blog_next2.get_previous_by_created_on()
    print(blog_next3)
    print(blog_next1, blog_next2, blog_next3)
    return render(request, 'blogsite.html', {'blog': blog,
                                             'blog_next1': blog_next1,
                                             'blog_next2': blog_next2,
                                             'blog_next3': blog_next3,})
