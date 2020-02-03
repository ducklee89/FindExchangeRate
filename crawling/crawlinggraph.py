import requests as rq
import time, json , requests
from django.http import  HttpResponse
from bs4 import BeautifulSoup
import urllib, csv
import pandas as pd # conda install pandas <= 설치되어 있음.
import re
from .models import exval
from django.shortcuts import render
import datetime
import pandas


# def graph(request) :



#     rows = .objects.all() #QuerySet
#     for t in rows : 
#         print("{},{},{}".format(t.id, t.name, t.age))
#         if 0<= t.age <=19 :
#             y[0] += 1
#         elif 20<= t.age <=29 :
#             y[1] += 1   
#         elif 30<= t.age <=39 :
#             y[2] += 1  
#         # 생략함.
        
#     #한글 폰트 사용하기
#     font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
#     rc('font', family=font_name)

#     plt.bar(x, y)
#     plt.title('AGES % PERSON')
#     plt.xlabel('AGES')
#     plt.ylabel('PERSON')

#     plt.draw() # 그래프 그리기
#     img = io.BytesIO() # 그린 그래프를 byte로 변경
#     plt.savefig(img, format="png") # png포멧으로 변경
#     graph_url = base64.b64encode(img.getvalue()).decode()
#     plt.close() #그래프 종료
#     return render(request, 'shop/graph.html', {"graph1":'data:image/png;base64,{}'.format(graph_url)})