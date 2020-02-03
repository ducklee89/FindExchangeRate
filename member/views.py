from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password

def signup(request):
    if request.method == "POST":
        if request.POST["pw"] == request.POST["pw_ck"]:
            user = User.objects.create_user(username=request.POST["username"],password=request.POST["pw"],first_name=request.POST['first_name'])
            auth.login(request,user)
            return redirect('/')
        return render(request, 'member/signup.html')
    return render(request, 'member/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pw']
        user = auth.authenticate(request, username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request, 'member/login.html', {'error' : '아이디.비번틀림'})
    else:
        return render(request, 'member/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def member_modify(request):
    if request.method == "POST":
        id = request.user.id
        user = User.objects.get(pk=id)
        user.first_name = request.POST["first_name"]
        user.save()
        return redirect('/')
    return render(request, 'member/member_modify.html')

def member_del(request):
    if request.method == "POST":
        pw_del = request.POST['pw_del']
        user = request.user
        if check_password(pw_del, user.password):
            user.delete()
            return redirect('/')
    return render(request, 'member/member_del.html')

def base(request):
    return render(request, 'member/base.html')



        
    
    



