from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#add first create
from django.contrib import admin
from visualizationapp import views
#we need all time for views.py
from urllib import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
#query ar jonno
from django.db.models import Q

from .models import *
from .forms import *


def dashboard(request):

    formfetch=EnergyProject.objects.all() 

    return render(request, 'dashboard.html', {'formfetch':formfetch})

def dashboard_delete(request,id):
    if request.method == 'POST':
        pi=EnergyProject.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/dashboard')


def dashboard_edit(request, id):
    if request.method == 'POST':
         pi=EnergyProject.objects.get(pk=id)
         fm=EnergyProjectForm(request.POST, instance=pi)
         if fm.is_valid():
             fm.save()  

    else:
           pi=EnergyProject.objects.get(pk=id)
           fm=EnergyProjectForm(instance=pi)
    

   
    context={'fo':fm,
             'pi':pi}      
    return render(request, 'edit.html', {'fo':fm})   


def filter_dashboard(request):

    formfetch=EnergyProject.objects.all() 

    if request.method == 'GET':
        queryone = request.GET.get('queryone')   #variable name those three query,queryx,queryday.Not form.py query
        querytwo=request.GET.get('querytwo')
        querythree=request.GET.get('querythree')
        queryfour=request.GET.get('queryfour')
        queryfive = request.GET.get('queryfive')   
        querysix=request.GET.get('querysix')
        queryseven=request.GET.get('queryseven')
        queryeight=request.GET.get('queryeight')
        querynine=request.GET.get('querynine')
        

        if queryone:
            products = EnergyProject.objects.filter(start_year__icontains=queryone).order_by('sector') 
            return render(request, 'filter_dashboardh.html', {'products':products})
        elif querytwo:
            products = EnergyProject.objects.filter(topic__icontains=querytwo).order_by('sector') 
            return render(request, 'filter_dashboard.html', {'products':products})
        elif querythree:
            products = EnergyProject.objects.filter(sector__icontains=querythree).order_by('sector') 
            return render(request, 'filter_dashboard.html', {'products':products})
        elif queryfour:
            products = EnergyProject.objects.filter(region__icontains=queryfour).order_by('sector') 
            return render(request, 'filter_dashboard.html', {'products':products})
        elif queryfive:
            products = EnergyProject.objects.filter(pestle__icontains=queryfive).order_by('sector') 
            return render(request, 'filter_dashboard.html', {'products':products})
        elif querysix:
            products = EnergyProject.objects.filter(source__icontains=querysix).order_by('sector') 
            return render(request, 'filter_dashboard.html', {'products':products})
        elif queryseven:
            products = EnergyProject.objects.filter(relevance__icontains=queryseven).order_by('sector') 
            return render(request, 'filter_dashboard.html', {'products':products})
        elif queryeight:
            products = EnergyProject.objects.filter(country__icontains=queryeight).order_by('sector') 
            return render(request, 'filter_dashboard.html', {'products':products})
        elif querynine:
            products = EnergyProject.objects.filter(likelihood__icontains=querynine).order_by('sector') 
            return render(request, 'filter_dashboard.html', {'products':products})
        else:
            print("No information to show")
            return render(request, 'filter_dashboard.html', {'formfetch':formfetch})
        

def line_chart(request):
    
    intensityone=EnergyProject.objects.filter(intensity=2).count()
    intensitytwo=EnergyProject.objects.filter(intensity=3).count()
    intensitythree=EnergyProject.objects.filter(intensity=4).count()
    intensityfour=EnergyProject.objects.filter(intensity=6).count()
    intensityfive=EnergyProject.objects.filter(intensity=8).count()
    intensitysix=EnergyProject.objects.filter(intensity=9).count()
    intensityseven=EnergyProject.objects.filter(intensity=10).count()
    intensityeight=EnergyProject.objects.filter(intensity=12).count()
    intensitynine=EnergyProject.objects.filter(intensity=16).count()
    intensityten=EnergyProject.objects.filter(intensity=20).count()
    intensityeli=EnergyProject.objects.filter(intensity=24).count()
    intensityelii=EnergyProject.objects.filter(intensity=32).count()
    intensityeliii=EnergyProject.objects.filter(intensity=48).count()
    intensityeliiii=EnergyProject.objects.filter(intensity=60).count()

    x=[intensityone,intensitytwo,intensitythree,intensityfour,intensityfive,intensitysix,intensityseven,intensityeight,
       intensitynine,intensityten,intensityeli,intensityelii,intensityeliii,intensityeliiii]
    
    return render(request, 'line_chart.html', {'x':x})

def yearchart(request):
    all=EnergyProject.objects.all()

#likelihood start with bar
    yearone=EnergyProject.objects.filter(end_year='2016').count()
    yeartwo=EnergyProject.objects.filter(end_year='2017').count()
    yearthree=EnergyProject.objects.filter(end_year='2018').count()
    yearfour=EnergyProject.objects.filter(end_year='2019').count()
    yearfive=EnergyProject.objects.filter(end_year='2020').count()
    yearsix=EnergyProject.objects.filter(end_year='2021').count()
    yearseven=EnergyProject.objects.filter(end_year='2024').count()
    yeareight=EnergyProject.objects.filter(end_year='2026').count()
    yearnine=EnergyProject.objects.filter(end_year='2028').count()
    yearten=EnergyProject.objects.filter(end_year='2034').count()
    yeareve=EnergyProject.objects.filter(end_year='2035').count()
    yearevee=EnergyProject.objects.filter(end_year='2035').count()
    yeareveee=EnergyProject.objects.filter(end_year='2036').count()
    yeareveeee=EnergyProject.objects.filter(end_year='2040').count()

    yearone=int(yearone)
    yeartwo=int(yeartwo)
    yearthree=int(yearthree)
    yearfour=int(yearfour)
    yearfive=int(yearfive)
    yearsix=int(yearsix)
    yearseven=int(yearseven)
    yeareight=int(yeareight)
    yearnine=int(yearnine)
    yearten=int(yearten)
    yeareve=int(yeareve)
    yearevee=int(yearevee)
    yeareveee=int(yeareveee)
    yeareveeee=int(yeareveeee)

    eve=[yearone,yeartwo,yearthree,yearfour,yearfive,yearsix,yearseven,yeareight,yearnine,yearten,yeareve,yearevee,yeareveee,
         yeareveee,yeareveeee]

    #for i in range(0, len(x)):
        #print(x[i])
    #end liklihood bar

 
    return render(request, 'yearchart.html',{'eve':eve})


def doughnutchart(request):

    ener=EnergyProject.objects.all()
    
    #for f in ener:
     #   print(f.region)   grate
         
    intensity=EnergyProject.objects.filter(intensity=72).count()
    intensity=int(intensity)

    # start relevance with doughnut
    ru=EnergyProject.objects.filter(country='Russia').count()
    ch=EnergyProject.objects.filter(country='Chine').count()
    un=EnergyProject.objects.filter(country='United State of America').count()
    ir=EnergyProject.objects.filter(country='Iran').count()
    br=EnergyProject.objects.filter(country='Brazil').count()
    ind=EnergyProject.objects.filter(country='India').count()
    li=EnergyProject.objects.filter(country='Libya').count()
    ma=EnergyProject.objects.filter(country='Malaysia').count()
    ni=EnergyProject.objects.filter(country='Nigeria').count()
    no=EnergyProject.objects.filter(country='Norway').count()
    sy=EnergyProject.objects.filter(country='Syria').count()
    co=EnergyProject.objects.filter(country='Colombia').count()
    leb=EnergyProject.objects.filter(country='Lebanon').count()
    indo=EnergyProject.objects.filter(country='Indonesia').count()
    egy=EnergyProject.objects.filter(country='Egypt').count()
    cana=EnergyProject.objects.filter(country='Canada').count()
    ang=EnergyProject.objects.filter(country='Angola').count()
    ira=EnergyProject.objects.filter(country='Iraq').count()
    aus=EnergyProject.objects.filter(country='Australia').count()
    afr=EnergyProject.objects.filter(country='Africa').count()
    jap=EnergyProject.objects.filter(country='Japan').count()
    moro=EnergyProject.objects.filter(country='Morocco').count()

    ru=int(ru)
    ch=int(ch)
    un=int(un)
    ir=int(ir)
    br=int(br)
    ind=int(ind)
    li=int(li)
    ma=int(ma)
    ni=int(ni)
    no=int(no)
    sy=int(sy)
    co=int(co)
    leb=int(leb)
    indo=int(indo)
    egy=int(egy)
    cana=int(cana)
    ang=int(ang)
    ira=int(ira)
    aus=int(aus)
    afr=int(afr)
    jap=int(jap)
    moro=int(moro)
    
    rel=[ru,ch,un,ir,br,ind,li,ma,ni,no,sy,co,leb,indo,egy,cana,ang,ira,aus,afr,jap,moro]
# end relevance   

    context={
        'ener':ener, 
        'intensity':intensity, 
         'rel':rel,
        }
    return render(request, "doughnutchart.html", context)

def allchart(request):

    all=EnergyProject.objects.all()

#likelihood start with bar
    likeone=EnergyProject.objects.filter(likelihood=1).count()
    liketwo=EnergyProject.objects.filter(likelihood=2).count()
    likethree=EnergyProject.objects.filter(likelihood=3).count()
    likefour=EnergyProject.objects.filter(likelihood=4).count()
    x=[likeone,liketwo,likethree,likefour]

    #for i in range(0, len(x)):
        #print(x[i])

#end liklihood bar

# start relevance with doughnut
    relevanceone=EnergyProject.objects.filter(relevance=1).count()
    relevancetwo=EnergyProject.objects.filter(relevance=2).count()
    relevancethree=EnergyProject.objects.filter(relevance=3).count()
    relevancefour=EnergyProject.objects.filter(relevance=4).count()
    relevancefive=EnergyProject.objects.filter(relevance=5).count()
    relevancesix=EnergyProject.objects.filter(relevance=6).count()
    
    rel=[relevanceone,relevancetwo,relevancethree,relevancefour,relevancefive,relevancesix]
# end relevance   

#Topic start
    oil=EnergyProject.objects.filter(topic='oil').count()
    oil=int(oil)
    aut=EnergyProject.objects.filter(topic='automaker').count()
    aut=int(aut)
    chang=EnergyProject.objects.filter(topic='change').count()
    chang=int(chang)
    energy=EnergyProject.objects.filter(topic='energy').count()
    energy=int(energy)
    gas=EnergyProject.objects.filter(topic='gas').count()
    gas=int(gas)
    growth=EnergyProject.objects.filter(topic='growth').count()
    growth=int(growth)
    workforce=EnergyProject.objects.filter(topic='workforce').count()
    workforce=int(workforce)
    emission=EnergyProject.objects.filter(topic='emission').count()
    emission=int(emission)
    production=EnergyProject.objects.filter(topic='production').count()
    production=int(production)
    policy=EnergyProject.objects.filter(topic='policy').count()
    policy=int(policy)
    consumption=EnergyProject.objects.filter(topic='consumption').count()
    consumption=int(consumption)
    vehicel=EnergyProject.objects.filter(topic='vehicel').count()
    vehicel=int(vehicel)
    agriculture=EnergyProject.objects.filter(topic='agriculture').count()
    agriculture=int(agriculture)
    technology=EnergyProject.objects.filter(topic='technology').count()
    technology=int(technology)
    debt=EnergyProject.objects.filter(topic='debt').count()
    debt=int(debt)
    captital=EnergyProject.objects.filter(topic='captital').count()
    captital=int(captital)
    wealth= EnergyProject.objects.filter(topic='wealth').count()
    wealth = int(wealth)

    #topic_list=['oil','aut','chang','energy','gas','growth','workforce','emission','production','policy','consumption','vehicel','agriculture',
    #           'technology','debt','captital','wealth']
    topic_num=[oil,aut,chang,energy,gas,growth,workforce,emission,production,policy,consumption,vehicel,agriculture,
               technology,debt,captital,wealth] 
    #topictwo=[oil,gas]   
    #for i in range(0, len(topic_num)):
        #print(topic_num[i])   great

    
#end topic
    context={
        'all':all, 
        'x':x, 
        'rel':rel,
        'topic_num':topic_num,
      

    }

 
    return render(request, "allchart.html", context)