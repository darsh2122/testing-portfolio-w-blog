from django.shortcuts import HttpResponse , render , get_object_or_404 
from .models import Post
# Create your views here.
def home(request):
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'latest':latest
    }
    return render(request,"index.html",context)
    
def blog(request):
    post_list = Post.objects.order_by('-timestamp')
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'queryset':post_list,
        'latest':latest,
    }
    return render(request ,"blog.html",context)

def post(request,id):
    post = get_object_or_404(Post , pk = id)
    context = { 
        'post':post
    }
    return render(request,"post.html",context)