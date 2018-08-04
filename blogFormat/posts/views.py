from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.

def posts_home(request):
    allPosts = Post.objects.all()
    query = request.GET.get("q")
    if query:
        allPosts = allPosts.filter(title__icontains=query)
    context = {"posts": allPosts}
    return render(request, "blog.html", context)

def post_detail(request, id=None):
    thisPost = get_object_or_404(Post, id=id)
    context = {"post": thisPost}
    return render(request, "post_detail.html", context)
    
def post_create(request):
    # if request.user.is_authenticated():
    form = PostForm()
    context = {
        "form": form
    }
    return render(request, "create_post.html", context)
    # else:
    #     return HttpResponse("<h1>Sorry you do not have access to this page!</h1>")

def post_update(request):
    return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello</h1>")