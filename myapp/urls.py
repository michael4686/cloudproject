from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('home',views.homepage,name="home"),
    path('studentsmarks',views.studentmark,name="marks"),
    path('',views.login,name="login"),
    path('add/',views.add,name="add"),
    path('rem/',views.rem,name="rem"),
    path('addrem/', views.add_rem_page, name='addrem'),
    
]