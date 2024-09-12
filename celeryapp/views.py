from django.shortcuts import render
from CELERYPRACTICE.celery import add
from celeryapp.tasks import sub
from celery.result import AsyncResult

# add is using delay(),
# Subtract is using apply_async(),
# both of them are same but apply_async() allow customization and options
def index(request):
 return render(request,'home.html')
def Add(request):
 result1=add.delay(10,30)
 return render(request,"home.html",{'result':result1})
def Subtract(request):
 result1=sub.apply_async(args=[100,20]) 
 print("Result",result1)
 return render(request,'home.html',{'result':result1})

def check_result(request,task_id):
 result=AsyncResult(task_id)
 print("Suceessul",result.ready())
 print("Suceessul",result.successful())
 return render(request,'result.html',{'result':result})