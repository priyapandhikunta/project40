from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# returning string as response by using FBV
def string_by_fbv(request):
    return HttpResponse('<h1>string_by_fbv</h1>')


# returning string as response by using CBV

class StringByCbv(View):
    def get(self,request):
        return HttpResponse('<h1>StringByCbv</h1>')

# returning html page as response by using FBV
def html_by_fbv(request):
    return render(request,'html_by_fbv.html')

# returning html page as response by using CBV

class HtmlBYCbv(View):
    def get(self,request):
        return render(request,'HtmlBYCbv.html')

# Inserting data into school by using FBV

def insert_by_fbv(request):
    d={'ESFO':SchoolForm()}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_by_fbv is done')
        else:
            return HttpResponse('insert_by_fbv is failed')
    return render(request,'insert_by_fbv.html',d)

# Inserting data into school by using CBV

class InsertByCbv(View):
    def get(self,request):
        d={'ESFO':SchoolForm()}
        return render(request,'InsertByCbv.html',d)
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_by_cbv is done')
        else:
            return HttpResponse('insert_by_cbv is failed')
    


class HtmlByTV(TemplateView):
    template_name='HtmlByTV.html'


