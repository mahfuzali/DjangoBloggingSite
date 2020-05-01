from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from posts.models import Post


def welcome(request):
    return render(request, "website/welcome.html",
                  {"posts": Post.objects.all()})
