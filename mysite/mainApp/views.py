from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html',{'values':['Hello. my tel','(068) 068-68-68' ,' admin@email.com'] } )    
    
    
    
    
# Create your views here.
