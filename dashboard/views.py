from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from posts.models import Post


@login_required(redirect_field_name='login/')
def dashboard(request):
    user_id = request.user.id
    posts = Post.objects.filter(user_id=user_id)
    return render(request, "dashboard/dashboard.html", {"userposts": posts})
