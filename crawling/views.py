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


def index(request):

    dt_index = pandas.date_range(start='20190101', end='20191208')
# pandas.date_range(start='20160901', end='20161031',freq='W-MON')
# 을 하면 해당 기간 매주 월요일들만 추출합니다.
# type(dt_index) => DatetimeIndex
# DatetimeIndex => list(str)
    dt_list = dt_index.strftime("%Y%m%d").tolist()

    for k in dt_list:
        # print(i)

        date = k
        url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=8WYTPowrz7mtIWE1yEP2VBPni7pVR1b8&searchdate="+date+"&data=AP01"    # 서버주소
        str1 = requests.get(url).text # 문자열
        dic = json.loads(str1) #[{},{},{},{},{}]

        # print(dic)
        for j, i in enumerate(dic):
            
            del i['yy_efee_r']
            del i['ten_dd_efee_r']

            # print(j, i)
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
            print(Exval.exval_id, Exval.exval_unit, Exval.exval_ttb, Exval.exval_tts, Exval.exval_deal, Exval.exval_bkpr, Exval.exval_kftc_bk, Exval.exval_kftc_de, Exval.exval_cur_nm )
            Exval.save()

    return HttpResponse('eeeee')

def dataframe_EXR(request):
    orderNum = int(request.GET.get('order',0))
    if orderNum == 1:
        data = list(exval.objects.all().order_by('-id').values())
    elif orderNum == 0:
        data = list(exval.objects.all().values())
    df = pd.DataFrame(data)
    notTableDataType = df.values.tolist() # df to list로 변경 [ [], [] ]
    return render(request,'crawling/dataframe.html', { "key":df.to_html(classes='table'), "key1":notTableDataType } )




# for key in var:
# print(key)
# print(var[key])



# a = dic['data']
# b = []
# for i in a:
#     b.append([ i['id'], i['name'], i['age'], i['height'], i['weight'] ])



# str1 = requests.get(url).text               # 문자열
# # print(type(str1),str1)

# dic = json.loads(str1) 
# list1 = []

# for row in dic:
#     result=row['result']
#     cur_unit=row['cur_unit']
#     print(result,cur_unit)

#   


#         for i, t in enumerate(b): #[ [],[],[],[],[] ]
#             if t[0] == a1:
#                 b[i] = [a1, a2, a3, a4, a5]
#                 break


        
#     elif menu == 4: #목록
#         print(b)

#     elif menu == 5: #저장
#         # 엑셀에서 한글 깨짐 방지 => 엔코딩을 cp949로 설정
#         f = open('c:/data/20191115.csv', 'w', encoding='utf-8', newline='') 
#         wr = csv.writer(f)
        
#         for tmp in b:
#             wr.writerow(tmp) #wr.writerow( ['a','가나다',34, 165.7, 56.6] )
#         f.close()

#     elif menu == 6:
#         f = open('c:/data/20191115.csv', 'r', encoding='utf-8')
#         rd = csv.reader(f)

#         b.clear()
#         for idx, tmp in enumerate(rd):
#             b.append( [ tmp[0], tmp[1], int(tmp[2]), float(tmp[3]), float(tmp[4]) ] )
#             print(idx, tmp)
        
# html = response.read()
# soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')

# links = soup.find_all('a',href=True)
# titles = soup.find_all('div',{'class':'line-gutter-backdrop'})
# title  = soup.find('td',{'class':'line-number'})





# a = str dic
# b = []
# for i in a:
#     b.append([ i['id'], i['name'], i['age'], i['height'], i['weight'], i['average'], i['sum'], i['else'], i['row'], i['type'], i['num'] ])

#     for idx, tmp in enumerate(b):
#         print(idx, tmp)
            # b.append( [ tmp[0], tmp[1], int(tmp[2]), float(tmp[3]), float(tmp[4]) ] )
            # print(idx, tmp)
        


