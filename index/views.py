from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password
import requests as rq
import time, json , requests
from django.http import  HttpResponse




# Create your views here.



def index(request):
    return render(request, 'index/index.html')




# def menubar(request):
#     br = dict.objects.all() # 모든 Border 테이블의 모든 object들을 br에 저장하라

#     b = request.GET.get('b','') # GET request의 인자중에 b 값이 있으면 가져오고, 없으면 빈 문자열 넣기

#     if b: # b에 값이 들어있으면 true
#         br = br.filter(title__icontains=b) # 의 title이 contains br의 title에 포함되어 있으면 br에 저장

#     return render(request, 'index/index.html', { 'border_search':br , 'b':b})
#     # br에는 Border 테이블에 title 이름이 'Singapore'인 데이터들이 들어있고,
#     # b에는 내가 처음에 입력했던 'Singapore'가 들어있다.