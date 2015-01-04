from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import Blog, Category, Comment


def index(request):

    posts = (Blog.objects.all()[:5])

    for post in posts:
        comments = Comment.objects.filter(related_post=post).count()
        post.comments = comments

    ctx = {
        'categories': Category.objects.all(),
        'posts': posts
    }

    return render_to_response('index.html', ctx, context_instance=RequestContext(request))


def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })


def about(request):
    return render_to_response('about.html', {})


def contact(request):
    return render_to_response('contact.html', {})