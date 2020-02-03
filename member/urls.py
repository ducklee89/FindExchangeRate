from django.urls import path
from .import views
# app_name='login'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('signout/', signout, name='signout'),
    path('member_modify/', views.member_modify, name='member_modify'),
    path('member_del', views.member_del, name='member_del'),
    path('base/', views.base, name='base')
    
    ]
