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



def index(request):
    date = "20020206"
    url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=8WYTPowrz7mtIWE1yEP2VBPni7pVR1b8&searchdate="+date+"&data=AP01"    # 서버주소
    str1 = requests.get(url).text # 문자열
    dic = json.loads(str1) #[{},{},{},{},{}]

    # print(dic)
    for j, i in enumerate(dic):
        
        del i['yy_efee_r']
        del i['ten_dd_efee_r']

        print(j, i)
        # print(type(text[i]),text[i])
    # 저장 : INSERT
        Exval = exval()
        Exval.exval_id = date+i['cur_unit']
        Exval.exval_unit = i['cur_unit']
        Exval.exval_ttb     = i['ttb'].replace(',','') if type(i['ttb']) != type(None) else '0'
        Exval.exval_tts     = i['tts'].replace(',','') if type(i['tts']) != type(None) else '0'
        Exval.exval_deal    = i['deal_bas_r'].replace(',','') if type(i['deal_bas_r']) != type(None) else '0'
        Exval.exval_bkpr = i['bkpr'].replace(',','') if type(i['bkpr']) != type(None) else '0'
        Exval.exval_kftc_bk = i['kftc_bkpr'].replace(',','') if type(i['kftc_bkpr']) != type(None) else '0'
        Exval.exval_kftc_de = i['kftc_deal_bas_r'].replace(',','') if type(i['kftc_deal_bas_r']) != type(None) else '0'
        Exval.exval_cur_nm = i['cur_nm']
        print(Exval.exval_ttb, Exval.exval_tts,Exval.exval_deal,Exval.exval_bkpr,Exval.exval_kftc_bk,Exval.exval_kftc_de  )
        Exval.save()

    return HttpResponse('eeeee')























