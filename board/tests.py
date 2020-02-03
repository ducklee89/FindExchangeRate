from django.test import TestCase
import requests, json, os
from collections import OrderedDict

# Create your tests here.


#https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=8WYTPowrz7mtIWE1yEP2VBPni7pVR1b8&searchdate=20191217&data=AP01
# url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=8WYTPowrz7mtIWE1yEP2VBPni7pVR1b8&searchdate=20191217&data=AP01'

def setConfig():
 # 키 불러오기 및 불러올 URL 설정
    f = open("C:/Users/admin/Documents/temp/ignore/keys", "r"); serviceKey = f.readline().strip()
    
    openApiUrl = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey='
    category_dataType = '&data=';  dataType = 'AP01' # 환율조회-타입코드
    # print(serviceKey, dataType)
    URL = openApiUrl + serviceKey + category_dataType + dataType
    return getData(URL)

def getData(url):
    return requests.get(url).json()

# response = setConfig()
url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=8WYTPowrz7mtIWE1yEP2VBPni7pVR1b8&searchdate=20191217&data=AP01'
response = requests.get(url).json() # docker
# print(response)

lists = []
for i in response :
    cur_data = OrderedDict()
    cur_data['exval_unit'] = i['cur_unit']
    cur_data['exval_deal'] = i['deal_bas_r'].replace(',','') if type(i['deal_bas_r']) != type(None) else '0'
    lists.append(OrderedDict.copy(cur_data))

for i in lists:
    print(i)
print(lists[0]['exval_deal'])


def CurrentExval():
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=8WYTPowrz7mtIWE1yEP2VBPni7pVR1b8&data=AP01'
    response = requests.get(url).json() # docker
    print(response)

    lists = []
    for i in response :
        cur_data = OrderedDict()
        cur_data['exval_unit'] = i['cur_unit']
        cur_data['exval_deal'] = i['deal_bas_r'].replace(',','') if type(i['deal_bas_r']) != type(None) else '0'
        lists.append(OrderedDict.copy(cur_data))
    return lists