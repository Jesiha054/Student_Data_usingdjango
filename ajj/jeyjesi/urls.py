from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('add/',views.add,name="add"),
    path('addsave/',views.addsave,name="addsave"),
    path('',views.listdata,name="listdata"),
    path('edit/<str:regno>/',views.edit,name="edit"),
    path('delete/<str:regno>/',views.delete,name="delete"),
]