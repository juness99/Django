from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.order_by("-id").all()#admin에서 불러온 게시글을 제일위로 정렬
    return render(request, "board/index.html", {"posts":posts})
    
def new(request):
    return render(request,"board/new.html")
    
def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    post = Post(title=title,content=content)
    post.save()
    
    return render(request, "board/create.html")
    
def read(request,id):
    post = Post.objects.get(pk=id)
    return render(request, "board/read.html",{"post":post})
    
def post_new(request):
    return render(request, "board/post_new.html")
    
def post_create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    
    post = Post(title=title, content = content)
    post.save()
    
    return render(request,"board/post_create.html")