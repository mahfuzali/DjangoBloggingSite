from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from posts.forms import MeetingForm
from posts.models import Post


def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "posts/detail.html", {"post": post})


@login_required(redirect_field_name='login/')
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "posts/new.html", {"form": form})
