from django.db import models, connection 
import matplotlib.pyplot as plt # 그래프 그리기
from matplotlib import font_manager, rc # 한글 적용폰트 설정
import io # 그래프를 byte로 변경
import base64 # 웹에서 출력하기위해
import requests, json, os
from collections import OrderedDict

# Create your models here.
class memoBoard(models.Model):
    objects         = models.Manager() # VS code 오류 제거용
    memo_no         = models.AutoField(primary_key=True)
    memo_id      = models.CharField(max_length=30)
    memo_priority   = models.CharField(max_length=30) # default : 4
    memo_productname= models.CharField(max_length=100)
    memo_cur_unit   = models.CharField(max_length=10)
    memo_price      = models.FloatField()
    memo_producturl = models.CharField(max_length=248)
    memo_memo       = models.CharField(max_length=100)
    memo_regdate    = models.DateTimeField(auto_now_add=True)
    memo_lastdate   = models.DateTimeField() # sysdate에서 더하기

    def __str__(self):
        return str(self.memo_no+", "+str(self.memo_priority)+", "+self.memo_productname)




class plotModel:
    def draw_plot(self,x,y, cur_unit):
        # 한글 폰트 사용하기
        font_name = font_manager.FontProperties(
            fname = "c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font',family=font_name)

        # plt.bar(x,y)
        plt.plot(x,y)
        plt.title(cur_unit)
        plt.xlabel('일주일간 동향')
        plt.ylabel('가격')
        plt.draw()          # 그래프 그리기
        img = io.BytesIO()  # 그린 그래프를 byte로 변경
        plt.savefig(img, format="png")
        graph_url = base64.b64encode(img.getvalue()).decode()
        plt.close()
        return 'data:image/png;base64,{}'.format(graph_url)

class CurrentExval:
    def currentExval(self):
        url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=8WYTPowrz7mtIWE1yEP2VBPni7pVR1b8&searchdate=20191217&data=AP01'
        ## 위 Test

        # url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=8WYTPowrz7mtIWE1yEP2VBPni7pVR1b8&data=AP01' # 11시 이전과 비영업일은 안됨.
        response = requests.get(url).json() # docker
        # print(response)

        lists = []
        for i in response :
            cur_data = OrderedDict()
            cur_data['exval_unit'] = i['cur_unit']
            cur_data['exval_deal'] = i['deal_bas_r'].replace(',','') if type(i['deal_bas_r']) != type(None) else '0'
            lists.append(OrderedDict.copy(cur_data))
        return lists