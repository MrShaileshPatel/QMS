from django.shortcuts import render
from .models import User
# Create your views here.

def home(request):
    if request.method == 'POST':
        name1  =  request.POST['name']
        contact1 = request.POST['contact']
        data1 = User( name = name1 , contact = contact1)
        data1.save()
        #data = { 'value' : 'Token genrated Successfully' }
        return render(request, 'index.html',  { "data" : "Token Generated" } )
    else:
        return render(request, 'index.html')

def display1(request):
    data = User.objects.all()
    return render(request, 'display.html',{'data' : data })

def token_admin(request):
    if request.method == 'POST':
        id = request.POST['id']
        instance  = User.objects.filter(id = id)
        instance.delete()
        data = User.objects.all()
        return render(request, 'token_admin.html',{'data' : data })
    else:
        data = User.objects.all()
        return render(request, 'token_admin.html',{'data' : data })
