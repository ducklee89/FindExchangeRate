from .serializers import MemoBoardSerializer, ExvalSerializer
from rest_framework.renderers import JSONRenderer

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt #의무화
from django.http import HttpResponse
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json


from .models import plotModel, memoBoard, CurrentExval
from crawling.models import exval 

plot = plotModel()  # plot 객체생성
memoB = memoBoard   # Model class
Exval = exval       # Model class
cuExval = CurrentExval()

# Create your views here.
def boardIndex(request):
    if request.method == "GET":
        if not request.user.is_authenticated: # 로그인 확인여부
            return redirect("/member/login")
        else:
            user = User.objects.get(username=request.user) # request.user = session에서 가져온것
            # print("id :",user) # id: a
            x = [7,6,5,4,3,2,1]
            # y = [0,0,0,0,0,0,0]
            y = [5,9,1,5,8,7,3]
            # date_yest = (datetime.now() + timedelta(days=-1)).strftime("%Y%m%d")
            # print("date_yest :",date_yest)
            
            # exvalObject = Exval.objects.filter(string__contains=)
            # exvalObject = Exval.objects.raw("select * from crawling_exval where exval_id like (select max(SUBSTR(EXVAL_ID,1,8)) as curdate from crawling_exval)||'{}'".format("%"))
            # exvalObject = Exval.objects.raw("select max(SUBSTR(EXVAL_ID,1,8)) as curdate from crawling_exval")
            
            # print("exvalObject:",exvalObject.columns, exvalObject)

            memoObj = memoB.objects.filter(memo_id=user) # 필요한 것만 셀렉트
            # serializer=MemoBoardSerializer(memoObj, many=True)
            # data = JSONRenderer().render(serializer.data)
            graph1 = plot.draw_plot(x,y,'화폐') # 호출
            return render(request, 'board/shop_item.html', {"graph1":graph1, "memodata":memoObj})



# # [{"id":"a"},{"id":"b"},{"id":"c"}] / 모범사례
# def index1(request):
#   obj = Student.objects.all()
#   serializer = StudentSerializer(obj, many=True)
#   data = JSONRenderer().render(serializer.data)
#   return HttpResponse(data)

@csrf_exempt
# @login_required
def insert(request):
    if request.is_ajax():
        date_str = datetime.now() + timedelta(days=3) # 현재로부터 3일후에 내가 지켜보고싶다고 가정.
        user = User.objects.get(username=request.user)
        # print("raw",date_str)
        # print("change",date_str.strftime("%Y-%m-%d"))
        # print("ajax data: ",request)
        m_id = user                         # 등록한 사용자이름
        name = request.POST['productname']  # 상품명
        url = request.POST['producturl']    # 주소
        cur_unit = request.POST['cur_unit'] # 화폐종류
        price = request.POST['price']       # 가격
        memo = request.POST['memo']         # 개인메모
        data = [name,cur_unit,price, url,memo]
        obj = memoB( memo_id = m_id
                    ,memo_priority = '4' 
                    ,memo_productname = name
                    ,memo_cur_unit = cur_unit
                    ,memo_price = price
                    ,memo_producturl = url
                    ,memo_memo = memo 
                    ,memo_lastdate = str(date_str.strftime("%Y-%m-%d %H:%M:%S"))
                    ) # set obj
        obj.save() # insert Query
        # return HttpResponse(status=200) # 나중에 ajax로 가져와서 모두 다시 할수 있다면 쓰기
        context = {"msg":"추가되었습니다!"}
        return HttpResponse(json.dumps(context), "application/json")
    else:
        return HttpResponse(json.dumps({"msg":"추가 실패..."}), "application/json")

@csrf_exempt
def delete(request):
    if request.is_ajax():
        user = User.objects.get(username=request.user)
        # print("delete / ",request, request.POST['memo_no'])
        m_id = user
        no = request.POST['memo_no']
        obj = memoB.objects.filter(memo_id=m_id).get(memo_no=no)
        obj.delete()
        return redirect('/board')

@csrf_exempt
def update(request):
    if request.is_ajax():
        print(request)
        user = User.objects.get(username=request.user)
        m_id = user
        no = request.POST['memo_no']
        productname = request.POST['productname']
        cur_unit = request.POST['cur_unit']
        producturl= request.POST['producturl']
        memo= request.POST['memo']
        obj = memoB.objects.filter(memo_id=m_id).get(memo_no=no)
        obj.memo_productname = productname
        obj.memo_cur_unit    = cur_unit
        obj.memo_producturl  = producturl
        obj.memo_memo        = memo
        obj.save()
        context= {'msg':"수정완료!"}
        return HttpResponse(json.dumps(context), "application/json")

@csrf_exempt
def exvalGraphList(request):
    if request.is_ajax():
        thisDay = str(datetime.now().strftime("%Y%m%d"))
        # print("exvalGraphList / 아작스 왔데이")
        cur_unit = request.POST['cur_unit']
        print("exvalGraphList :", cur_unit)
        querry=r"""select * from (select * from crawling_exval where EXVAL_UNIT = %s order by exval_id desc) where rownum <= 6"""
        exvalObject = Exval.objects.raw(querry, [cur_unit])
        # serializer = ExvalSerializer(exvalObject, many=True)
        # data = JSONRenderer().render(serializer.data)
        # x = [5,4,3,2,1]
        # y = [1,5,8,7,3]
        x=[]
        y=[]
        for p in exvalObject:
            x.append(str(p)[:8])
            y.append(p.exval_deal)
            # print(p, p.exval_deal)
        x.reverse(); y.reverse()
        curData = cuExval.currentExval() # [ ()() ] curData['exval_deal']
        for p in curData:
            if p['exval_unit'] == cur_unit:
                deal = float(p['exval_deal']) # float 안해주면 정렬되어 들어가서 모두 직선이됨.
                break
        x.append(thisDay); y.append(deal)
        graph = plot.draw_plot(x,y,cur_unit)
        context = {"src":graph}
        return HttpResponse(json.dumps(context), "application/json")

@csrf_exempt
def exvalBoardList(request):
    if request.is_ajax():
        querry=r"""select * from crawling_exval where exval_id like (select max(SUBSTR(EXVAL_ID,1,8)) as curdate from crawling_exval)||'%%'
            """
        exvalObject = Exval.objects.raw(querry)
        serializer = ExvalSerializer(exvalObject, many=True)
        data = JSONRenderer().render(serializer.data)
        print("exvalList :",data)
        return HttpResponse(data)

@csrf_exempt
def exvalCurrentData(request):
    if request.is_ajax():
        data = cuExval.currentExval()
        # print("exvalCurrentData / 아작스 왔데이")
        return HttpResponse(json.dumps(data), "application/json")

def memolist(request):
    if request.is_ajax():
        obj = memoB.objects.all()
        serializer=MemoBoardSerializer(obj, many=True)
        data = JSONRenderer().render(serializer.data)
        print("memolist :",data)
        return HttpResponse(data)
        # return HttpResponse(json.dump(data))




######## test ####### 
@csrf_exempt
def edit_favorites(request): # http://127.0.0.1:8000/board/edit_favorites
    
    if request.is_ajax():
        message = "Yes, AJAX!"
    elif request.method == 'GET':
        return render(request, 'ajax.html')
    else:
        message = "Not Ajax"
    return HttpResponse(message)

def test_graph(request):
    x = [10,20,30,40,50,60,70]
    # y = [0,0,0,0,0,0,0]
    y = [5,9,1,5,8,7,3]

    graph1 = plot.draw_plot(x,y,'화폐')
    return render(request, 'board/text.html', {"graph1":graph1})