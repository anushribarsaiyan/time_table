from django.shortcuts import render,redirect
from .forms import *

def create_timetable(request):
    form = time_table_form()
    if request.method == 'POST':
        form = time_table_form(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'new1.html',context)
def table(request):
    data=time_table.objects.all()
    return render(request,'index.html',{'data':data})
def updatetime(request,pk ):
    time=time_table.objects.get(id=pk)
    form=time_table_form(instance=time)
    if request.method == 'POST':
        form = time_table_form(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'new1.html',context)
def deletetime(request,pk):
    order = time_table.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('table')
    context={'item':order}
    return render(request,'delete.html',context)

def login(request):
    return render(request,'login.html')
def Register(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save(login)
    context={'form':form}
    return render(request,'Rwgister.html',context)
