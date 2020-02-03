from django.urls import path

from . import views # 현재 패키지에서 views 모듈을 가져옴

urlpatterns = [
      path('',  views.boardIndex,  name='boardIndex')
     ,path('insert', views.insert, name="insert")
     ,path('delete', views.delete, name="delete")
     ,path('update', views.update, name="update")
     ,path('exvalBoardList', views.exvalBoardList, name="exvalBoardList")
     ,path('exvalGraphList', views.exvalGraphList, name="exvalGraphList")
     ,path('exvalCurrentData', views.exvalCurrentData, name="exvalCurrentData")

     ###### test #####
     ,path('edit_favorites',  views.edit_favorites,  name='edit_favorites')
     ,path('test_graph',  views.test_graph,  name='test_graph')
]