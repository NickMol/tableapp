from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import JsonResponse

# Create your views here.

def table1(request):
    context = {}
    return render(request, 'table/table1.html',context)

def table2(request):
    context = {}
    return render(request, 'table/table2.html',context)

def home(request):
    
    context = {
                }
    return render(request, 'table/home.html',context)


def modelmultiplechoicefield(request):
    form = TableDataForm(request.POST or None)
    if request.POST and form.is_valid():
        name = form.cleaned_data['name']
        stadium = form.cleaned_data['stadium']
        attendance = form.cleaned_data['attendance']
        
        obj = TableData(
            name=name, 
            stadium = stadium, 
            attendance = attendance,
        )

        obj.save()
        form2 = TableDataForm(request.POST, instance=obj)
        form2.save(commit=False)
        form2.save_m2m()
        return redirect('home')

    context = {'form':form}
    return render(request, 'table/modelmultiplechoicefield.html',context)

def footballclubs(request):
    result_list = list(TableData.objects.all()\
                .values('name', 
                        'attendance',
                        'stadium',
                        'created_at',
                        'edited_at',
                        'id',
                       ))
  
    return JsonResponse(result_list, safe=False)
