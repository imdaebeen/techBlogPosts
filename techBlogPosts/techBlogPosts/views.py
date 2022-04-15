from django.shortcuts import render
from . import posts

def index(request):

    title = posts.getPosts()

    return render(request,'index.html',{'title':title})