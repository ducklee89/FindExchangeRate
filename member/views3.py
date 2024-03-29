from django.shortcuts import render
from .forms import SigninForm, SignupForm #이전에 만든 form 클래스를 선언해주고
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth.models import User #User 모델을 사용하기위해 선언해준다.

def signup(request):#역시 GET/POST 방식을 사용하여 구현한다.
    if request.method == "GET":
        return render(request, 'member/signup.html', {'f':SignupForm()} )
    
    
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password']  == form.cleaned_data['password_check']:
#cleaned_data는 사용자가 입력한 데이터를 뜻한다.
#즉 사용자가 입력한 password와 password_check가 맞는지 확인하기위해 작성해주었다.

                new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])
#User.object.create_user는 사용자가 입력한 name, email, password를 가지고 아이디를 만든다.
#바로 .save를 안해주는 이유는 User.object.create를 먼저 해주어야 비밀번호가 암호화되어 저장된다.

                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
#나머지 입력하지 못한 last_name과, first_name은 따로 지정해준다.
                new_user.save()
                
                return render(request, 'index/index.html')
            else:
                return render(request, 'member/signup.html',{'f':form, 'error':'비밀번호와 비밀번호 확인이 다릅니다.'})#password와 password_check가 다를 것을 대비하여 error를 지정해준다.

        else: #form.is_valid()가 아닐 경우, 즉 유효한 값이 들어오지 않았을 경우는

            return render(request, 'member/signup.html',{'f':form})
#원래는 error 메시지를 지정해줘야 하지만 따로 지정해주지 않는다.
#그 이유는 User 모델 클래스에서 자동으로 error 메시지를 넘김

from django.contrib.auth import login, authenticate
#login과 authenticate 기능을 사용하기위해 선언
#login은 login처리를 해주며, authenticate는 아이디와 비밀번호가 모두 일치하는 User 객체를 추출
def signin(request):#로그인 기능
    if request.method == "GET":
        return render(request, 'member/signin.html', {'f':SigninForm()} )

    elif request.method == "POST":
        form = SigninForm(request.POST)
        id = request.POST['username']
        pw = request.POST['password']
        u = authenticate(username=id, password=pw)
#authenticate를 통해 DB의 username과 password를 클라이언트가 요청한 값과 비교한다.
#만약 같으면 해당 객체를 반환하고 아니라면 none을 반환한다.
        if u: #u에 특정 값이 있다면
            login(request, user=u) #u 객체로 로그인해라
            return render(request, 'index/index.html')
        else:
            return render(request, 'member/signin.html',{'f':form, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})

from django.contrib.auth import logout #logout을 처리하기 위해 선언
def signout(request): #logout 기능
    logout(request) #logout을 수행한다.
    return render(request, 'index/index.html')

# 회원정보 수정 
from django.contrib.auth.forms import UserChangeForm

def member_modify(request):
    if request.method == "post":
        id = request.user.id
        user = user.object.get(pk=id)
        user.first_name = request.POST["first_name"]
        user.save()
    return render(request, 'member/member_modify.html')
