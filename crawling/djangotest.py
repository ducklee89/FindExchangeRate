from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from base64 import b64encode

# from .models import Item
# from .models import Student #model 추가

@csrf_exempt
def insert_multi(request) :
    if request.method == "GET" :
        return render(request, 'shop/insert_multi.html')
    elif request.method == "POST" :
        id = request.POST['id']
        na = request.POST['na']
        ag = request.POST['ag']

        obj = Student(id=id, name=na, age=ag )
        obj.save()
        return redirect("/shop/insert_multi")


##template/shop/insert_multi.html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <title><Document</title>
# </head>


    # def __str__(self):
    #     return str(self.itm_no) #문자만 가능


#view
@csrf_exempt

def delete_multi(request) :
    if request.method == "GET" :
        rows = Student.objects.all()
        print( type(rows[0]) )
        rows1 = Student.objects.raw("SELECT * FROM SHOP_STUDENT")
        print( type(rows1[0]) )
        return render(request, 'shop/delete_multi.html', {"data":rows1})

    elif request.method == "POST":
        chk = request.POST.getlist("chk[]")
        print(chk)
        #Student.objects.filter(id__in=[삭제하고자 id 리스트])
        #DELETE FROM SHOP_STUDENT WHERE ID IN (삭제할 ID 리스트)
        Student.objects.filter(id__in=chk).delete()
        return redirect("/shop/delete_multi")




