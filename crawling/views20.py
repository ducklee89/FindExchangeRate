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


text=[
    {'result': 1, 'cur_unit': 'AED', 'ttb': '354.37', 'tts': '361.51', 'deal_bas_r': '357.94', 'bkpr': '357', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '357', 'kftc_deal_bas_r': '357.94', 'cur_nm': '아랍에미리트 디르함'}, {'result': 1, 'cur_unit': 'ATS', 'ttb': '82.09', 'tts': '83.73', 'deal_bas_r': '82.91', 'bkpr': '82','yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '82', 'kftc_deal_bas_r': '82.91', 'cur_nm': '오스트리아 실링'},
 {'result': 1, 'cur_unit': 'AUD', 'ttb': '663.34', 'tts': '676.74', 'deal_bas_r': '670.04', 'bkpr': '670', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '670', 'kftc_deal_bas_r': '670.04', 'cur_nm': '호주 달러'},
  {'result': 1, 'cur_unit': 'BEF', 'ttb': '28', 'tts': '28.56', 'deal_bas_r': '28.28', 'bkpr': '28', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '28', 'kftc_deal_bas_r': '28.28', 'cur_nm': '벨기에 프랑'},
  {'result': 1, 'cur_unit': 'BHD', 'ttb': '3,451.95', 'tts': '3,521.67', 'deal_bas_r': '3,486.81', 'bkpr': '3,486','yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '3,486', 'kftc_deal_bas_r': '3,486.81', 'cur_nm': '바레인 디나르'}, {'result': 1, 'cur_unit': 'CAD', 'ttb': '814.85', 'tts': '831.31', 'deal_bas_r': '823.08', 'bkpr': '823', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '823', 'kftc_deal_bas_r': '823.08', 'cur_nm': '캐나다 달러'},
   {'result': 1, 'cur_unit': 'CHF', 'ttb': '736.82', 'tts': '751.7', 'deal_bas_r': '744.26', 'bkpr': '744', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '744', 'kftc_deal_bas_r': '744.26', 'cur_nm': '스위스 프랑'}, 
  {'result': 1, 'cur_unit': 'CNY', 'ttb': '157.27', 'tts': '160.43', 'deal_bas_r': '158.85', 'bkpr':'158', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '158', 'kftc_deal_bas_r': '158.85', 'cur_nm': '중국 위안'}, {'result': 1, 'cur_unit': 'DEM', 'ttb': None, 'tts': None, 'deal_bas_r': '583.33', 'bkpr': None, 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': None, 'kftc_deal_bas_r': '583.33', 'cur_nm': '독일 마르크'}, 
  {'result': 1, 'cur_unit': 'DKK', 'ttb': '152.03', 'tts': '155.09', 'deal_bas_r': '153.56', 'bkpr': '153', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '153', 'kftc_deal_bas_r': '153.56', 'cur_nm': '덴마아크 크로네'}, {'result': 1, 'cur_unit': 'ESP(100)', 'ttb': '67,884', 'tts': '69,254', 'deal_bas_r': '68,569', 'bkpr': '68,500', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '68,500', 'kftc_deal_bas_r': '68,569', 'cur_nm': '스페인 페세타'}, {'result': 1, 'cur_unit': 'EUR', 'ttb': '1,129.5', 'tts': '1,152.3', 'deal_bas_r': '1,140.9', 'bkpr': '1,140', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '1,140', 'kftc_deal_bas_r': '1,140.9', 'cur_nm': '유로'}, 
  {'result': 1, 'cur_unit': 'FIM', 'ttb': '189.98', 'tts': '193.8', 'deal_bas_r': '191.89', 'bkpr': '191', 'yy_efee_r': None, 'ten_dd_efee_r': None,'kftc_bkpr': '191', 'kftc_deal_bas_r': '191.89', 'cur_nm': '핀란드 마르카'}, {'result': 1, 'cur_unit': 'FRF', 'ttb': '172.2', 'tts': '175.66', 'deal_bas_r': '173.93','bkpr': '173', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '173', 'kftc_deal_bas_r': '173.93', 'cur_nm': '프랑스 프랑'}, 
  {'result': 1, 'cur_unit': 'GBP', 'ttb': '1,842.36', 'tts': '1,879.56', 'deal_bas_r': '1,860.96', 'bkpr': '1,860', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '1,860', 'kftc_deal_bas_r': '1,860.96', 'cur_nm': '영국 파운드'}, {'result': 1, 'cur_unit': 'HKD', 'ttb': '166.88', 'tts': '170.24', 'deal_bas_r': '168.56', 'bkpr': '168', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '168', 'kftc_deal_bas_r': '168.56', 'cur_nm': '홍콩 달러'}, 
  {'result': 1, 'cur_unit': 'IDR(100)', 'ttb': '12.64', 'tts': '12.88', 'deal_bas_r': '12.76', 'bkpr': '12', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '12', 'kftc_deal_bas_r': '12.76', 'cur_nm': '인도네시아 루피아'}, {'result': 1, 'cur_unit': 'ITL(100)', 'ttb': '58.34', 'tts': '59.5', 'deal_bas_r': '58.92', 'bkpr': '58', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '58', 'kftc_deal_bas_r':
'58.92', 'cur_nm': '이태리 리라'}, {'result': 1, 'cur_unit': 'JPY(100)', 'ttb': '972.25', 'tts': '991.89', 'deal_bas_r': '982.07', 'bkpr': '982', 'yy_efee_r': '1.0925', 'ten_dd_efee_r': '0.02731', 'kftc_bkpr': '982', 'kftc_deal_bas_r': '982.07', 'cur_nm': '일본 옌'}, {'result': 1, 'cur_unit': 'KRW', 'ttb': None, 'tts': None, 'deal_bas_r': '1', 'bkpr': '1', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '1', 'kftc_deal_bas_r': '1', 'cur_nm': '한국 원'}, {'result': 1, 'cur_unit': 'KWD', 'ttb': '4,226.1', 'tts': '4,311.46', 'deal_bas_r': '4,268.78', 'bkpr': '4,268', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '4,268', 'kftc_deal_bas_r': '4,268.78', 'cur_nm': '쿠웨이트 디나르'}, {'result': 1, 'cur_unit': 'MYR', 'ttb': '342.52', 'tts': '349.42', 'deal_bas_r': '345.97', 'bkpr': '345', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '345', 'kftc_deal_bas_r': '345.97', 'cur_nm': '말레이지아 링기트'}, {'result': 1, 'cur_unit': 'NLG', 'ttb': None, 'tts': None, 'deal_bas_r': '517.71', 'bkpr': None, 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': None, 'kftc_deal_bas_r': '517.71', 'cur_nm': '네델란드 길더'}, {'result': 1, 'cur_unit': 'NOK', 'ttb': '143.72', 'tts': '146.62', 'deal_bas_r': '145.17', 'bkpr': '145', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '145', 'kftc_deal_bas_r': '145.17', 'cur_nm': '노르웨이 크로네'}, {'result': 1, 'cur_unit': 'NZD', 'ttb': '541.91', 'tts': '552.85', 'deal_bas_r': '547.38', 'bkpr': '547', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '547', 'kftc_deal_bas_r': '547.38', 'cur_nm': '뉴질랜드 달러'}, {'result': 1, 'cur_unit': 'SAR', 'ttb': '347.11', 'tts': '354.11', 'deal_bas_r': '350.61', 'bkpr': '350', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '350', 'kftc_deal_bas_r': '350.61', 'cur_nm': '사우디 리얄'}, {'result': 1, 'cur_unit': 'SEK', 'ttb': '122.34', 'tts': '124.8', 'deal_bas_r': '123.57', 'bkpr': '123', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '123', 'kftc_deal_bas_r': '123.57', 'cur_nm': '스웨덴 크로나'}, {'result': 1, 'cur_unit': 'SGD', 'ttb': '709.36', 'tts': '723.68', 'deal_bas_r': '716.52', 'bkpr': '716', 'yy_efee_r': None,
'ten_dd_efee_r': None, 'kftc_bkpr': '716', 'kftc_deal_bas_r': '716.52', 'cur_nm': '싱가포르 달러'}, {'result': 1, 'cur_unit': 'THB', 'ttb': '29.61', 'tts': '30.19', 'deal_bas_r': '29.9', 'bkpr': '29', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '29', 'kftc_deal_bas_r': '29.9', 'cur_nm': '태국 바트'}, {'result': 1, 'cur_unit': 'USD', 'ttb': '1,301.56', 'tts': '1,327.84', 'deal_bas_r': '1,314.7', 'bkpr': '1,314', 'yy_efee_r': '2.9', 'ten_dd_efee_r': '0.08055', 'kftc_bkpr': '1,314', 'kftc_deal_bas_r': '1,314.7', 'cur_nm': '미국 달러'}, {'result': 1, 'cur_unit': 'XOF', 'ttb': None, 'tts': None, 'deal_bas_r': '1.7393', 'bkpr': '1', 'yy_efee_r': None, 'ten_dd_efee_r': None, 'kftc_bkpr': '1', 'kftc_deal_bas_r': '1.7393', 'cur_nm': '씨에프에이 프랑(비씨에이오)'}]


for j, i in enumerate(text): #[ {},{} ]
    # for i in text:
    # print(j, i) # {}
    

    print(j, i)

str1 = requests.get(url).text # 문자열
dic = json.loads(str1) #[{},{},{},{},{}]

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=8WYTPowrz7mtIWE1yEP2VBPni7pVR1b8&searchdate="+date+"&data=AP01"'






# for b in i: #{}  dict1['result']   =>  i[b]
# print(b) result 
# print(i[b]) # value
# print(i['cur_unit'])

# print(text[2]['cur_unit'])# {}


   







# print(text[0]['result'])
# print(text[0]['cur_unit'])
# print(text[0]['ttb'])
# print(text[0]['tts'])
# print(text[0]['deal_bas_r'])

#save

