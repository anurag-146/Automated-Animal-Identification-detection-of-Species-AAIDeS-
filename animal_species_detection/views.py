from django.http import HttpResponse
from  django.shortcuts import render
from . import models
import mysql.connector as mycon
 
def index(request):
    return render(request, "index.html")
 
def upload(request):
    if request.method == 'POST':
         
        photo=models.handle_uploaded_file1(request.FILES['file']) 
        cate,cate1,filename=photo.split('|')
    return render(request, "Success.html",{"category":cate,"category1":cate1,"filename":filename})