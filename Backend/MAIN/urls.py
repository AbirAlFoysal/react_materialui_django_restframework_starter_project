from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from demo_crud import views

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home, name="home"),
    path('democrud/', views.CrudTable.as_view(), name="demo_crud"),
    path('democrudupdate/<int:pk>/', views.CrudTableUpdate.as_view(), name="demo_crud_update"),

]
