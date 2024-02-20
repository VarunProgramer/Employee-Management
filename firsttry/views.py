from django.shortcuts import render, redirect
from firsttry.models import empdetails
from firsttry.forms import empform

# Create your views here.

def home(request):
    emp = empdetails.objects.all()
    data_list = {
        'emp_list' : emp
    }
    return render(request, 'firsttry/intex.html', context = data_list)

def delete(request, id):
    emp = empdetails.objects.get(id = id)
    emp.delete()
    return redirect('/')

def create(request):
    form = empform()
    if request.method == 'POST':
        form = empform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')
    return render(request, 'firsttry/create.html',{'form' : form})

def edit (request, id):
    form = empdetails.objects.get(id = id)
    if request.method == 'POST':
        form = empform(request.POST, instance = form)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'firsttry/edit.html', {'form' : form})
