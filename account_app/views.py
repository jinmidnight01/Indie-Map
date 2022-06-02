from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import User

# Create your views here.

@login_required(login_url='/accounts/naver/login/')
def userpage(request):
    user = request.user
    return redirect('mypage', user.id)

@login_required(login_url='/accounts/naver/login/')
def mypage(request, user_id):
    person = get_object_or_404(get_user_model(), id=user_id)
    people = User.objects.all()
    return render(request, 'mypage.html', {'person' : person, 'people': people})

@login_required(login_url='/accounts/naver/login/')
def transition(request):
    user = request.user
    if user.status == 0:
        user.status = 1
        user.save()
    else:
        user.status = 0
        user.save()
    return redirect('mypage', user.id)

@login_required(login_url='/accounts/naver/login/')
def edit(request):
    user = request.user
    if request.method == "GET":
        return render(request, "edit.html")
    else:
        user.name = request.POST['name']
        user.intro = request.POST['intro']
        user.insta = request.POST['insta']
        user.youtube = request.POST['youtube']
        try:
            user.image = request.FILES['image']
            user.save()
        except:
            user.save()
        return redirect('mypage', user.id)

@login_required(login_url='/accounts/naver/login/')
def follow(request, user_id):
    person = get_object_or_404(get_user_model(), id=user_id)
    if request.user in person.follower.all():
        person.follower.remove(request.user)
        person.save()
    else:
        person.follower.add(request.user)
        person.save()
    return redirect('mypage', user_id)

from allauth.socialaccount.models import SocialAccount

def callback(request):
    social_user = SocialAccount.objects.all()
    return render(request, 'callback.html', {'social_user' : social_user})