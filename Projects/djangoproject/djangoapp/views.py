from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    if request.method == 'POST':
         form = Studeinfoform(request.POST)
         if form.is_valid():
              form.save()
              print('Data instered')
         else:
              print(form.errors) 
    return render(request, 'index.html')

def showdata(request):
     stdata = Studeinfo.objects.all()
     return render(request,'showdata.html', {'stdata': stdata})

def deletedata(request,id):
     stid = Studeinfo.objects.get(id=id)
     Studeinfo.delete(stid)
     return redirect('showdata')
   
def updatedata(request,id):
     stid = Studeinfo.objects.get(id=id)
     if request.method == 'POST':
         form = Studeinfoform(request.POST, instance=stid)
         if form.is_valid():
              form.save()
              print('Record update')
              return redirect('showdata')
         else:
              print(form.errors) 
     return render(request,'updatedata.html',{'stid':stid})
     
    