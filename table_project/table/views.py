from django.shortcuts import render

# Create your views here.

def table1(request):
    
    context = {
                }
    return render(request, 'table/table1.html',context)

def home(request):
    
    context = {
                }
    return render(request, 'table/home.html',context)


