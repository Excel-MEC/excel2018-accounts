from django.shortcuts import render
from django.views.generic import TemplateView
from register.forms import RegistrationForm, PaidRegistrationForm, StudentForm
import string
from django.http import JsonResponse
from register.models import userinfo,winners,paid_userinfo,paid_winners
import pyqrcode
import sys
from django.http import HttpResponseRedirect
import random

def genexid(size=4, nums=string.digits):
	exid=''
	for _ in range(size):
	 exid += random.choice(nums)
	return exid

def uniqueid(x):
        code=  x + genexid()
        qs = userinfo.objects.filter(excelid=code).exists()
        if qs:
            uniqueid()
        return code

class RegView(TemplateView):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        context = {
           "title": "testing",
           "form": form
        }
        return render(request, "home.html", context)

    def post(self,request,*args,**kwargs):
        context = {
		"title": "testing",
		"form": form
		}
        if form.is_valid():
            mail = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            college = form.cleaned_data.get('college')
            stay1 = form.cleaned_data.get('stay') 
            code = uniqueid('6')
            u = userinfo(excelid=code, name=name, college=college, email=mail, phone=phone, stay=stay1)
            u.save()
			# obj=userinfo.objects.get(email=mail)
			# im=pyqrcode.create(obj.excelid)
			# im.svg('static/qrcodes/%s.svg'%(obj.excelid),scale=20)
            return render(request,"success.html",{"name":name})

        return render(request,"home.html",context)

class PaidReg(TemplateView):
    def get(self, request, *args, **kwargs):
        form = PaidRegistrationForm()
        context={
		"title":"testing",
		"form":form
		}
        return render(request,"paidreg.html",context)
    
    def post(self, request, *args, **kwargs):
        form = PaidRegistrationForm(request.POST)
        context={
		"title":"testing",
		"form":form
		}

        if form.is_valid():
            mail=form.cleaned_data.get('email')
            name=form.cleaned_data.get('name')
            phone=form.cleaned_data.get('phone')
            college=form.cleaned_data.get('college')
            stay=form.cleaned_data.get('stay')
            event=form.cleaned_data.get('event')
            code=uniqueid('7')
            u=paid_userinfo(excelid=code,name=name,college=college,email=mail,phone=phone,event=event,stay=stay,present=True)
            u.save()
            #flag for offlinereg or paidreg
            flag            
            context = {
	            "excelid":code,
	            "flag" : flag 
            }
            return render(request,"excelid.html",context)
        return render(request,"paidreg.html",context)

class OfflineReg(TemplateView):
	def get(self,request,*args,**kwargs):
		form=RegistrationForm()
		context={
		"title":"testing",
		"form":form
		}
		return render(request,"offlinereg.html",context)

	def post(self,request,*args,**kwargs):
		form=RegistrationForm(request.POST)
		context={
		"title":"testing",
		"form":form
		}

		if form.is_valid():
			mail=form.cleaned_data.get('email')
			name=form.cleaned_data.get('name')
			phone=form.cleaned_data.get('phone')
			college=form.cleaned_data.get('college')
			stay=form.cleaned_data.get('stay')
			code=uniqueid('6')
			u=userinfo(excelid=code,name=name,college=college,email=mail,phone=phone,stay=stay,present=True)
			u.save()
			#flag for offlinereg or paidreg
			flag=0

			context = {
				"excelid":code,
				"flag" : flag 
			}
			return render(request,"excelid.html",context)
		return render(request,"offlinereg.html",context)

class SchoolReg(TemplateView):
	def get(self,request,*args,**kwargs):
		form=StudentForm()
		context={
		"title":"testing",
		"form":form
		}
		return render(request,"studentreg.html",context)

	def post(self,request,*args,**kwargs):
		form=StudentForm(request.POST)
		context={
		"title":"testing",
		"form":form
		}

		if form.is_valid():
			name=form.cleaned_data.get('Name')
			college=form.cleaned_data.get('College')
			code=uniqueid('9')
			u=userinfo(excelid=code,name=name,college=college,stay=False,present=True)
			u.save()
			#flag for offlinereg or paidreg
			flag=2

			context = {
				"excelid":code,
				"flag" : flag 
			}
			return render(request,"excelid.html",context)
		return render(request,"studentreg.html",context)

def Certi(request):

	error1=False
	sb=0
	result=0
	if request.method == 'POST':
		if request.POST.get('certificate'):
			certificate=request.POST.get('certificate')
			list=certificate.split(',')
			obj=winners.objects.get(excelid=list[0],event=list[1])
			obj.printed = not obj.printed
			obj.save()
			d=[]
			data={
			'dataset':d
			}
			return JsonResponse(data)
		if request.POST.get('certificate1'):
			certificate=request.POST.get('certificate1')
			obj=userinfo.objects.get(excelid=certificate)
			obj.printed = not obj.printed
			obj.save()
			d=[]
			data={
			'dataset':d
			}
			return JsonResponse(data)
		if request.POST.get('value'):
			value=request.POST.get('value')
			result=userinfo.objects.filter(excelid=value)
			if(len(result)==0):
				result=paid_userinfo.objects.filter(excelid=value)
			sb=1
			if(len(result)==0):
				error1=True
				sb=0

		if request.POST.get('paid_short'):	
			paid_short=request.POST.get('paid_short')
			obj=paid_userinfo.objects.get(excelid=paid_short)
			obj.printed = not obj.printed
			obj.save()
			d=[]
			data={
			'dataset':d
			}
			return JsonResponse(data)
		if request.POST.get('paid_win'):
			paid_win=request.POST.get('paid_win')
			list=paid_win.split(',')
			obj=paid_winners.objects.get(excelid=list[0],event=list[1])
			obj.printed = not obj.printed
			obj.save()
			d=[]
			data={
			'dataset':d
			}
			return JsonResponse(data)
		

	win = winners.objects.all()
	paid_win = paid_winners.objects.all()
	paid_usr = paid_userinfo.objects.all()
	win1=win.exclude(college = "Model Engineering College")
	usr = userinfo.objects.exclude(college = "Model Engineering College")
	context = {
	"sb":sb,
	"obj":result,
	"win_obj": win1,
	"paid_win_obj": paid_win,
	"paid_usr":paid_usr,
	"usr": usr,
	"error1":error1
	}
	return render(request,"certificate.html",context)

class SearchByView(TemplateView):
	def get(self,request,*args,**kwargs):
		searchby="phone"
		context={
		"title":"testing",
		"searchby":searchby
		}
		return render(request,"searchby.html",context)

	def post(self,request,*args,**kwargs):
		error1=False
		error2=False
		result=[]
		sb=-1
		searchby=request.POST.get('searchby')
		value=request.POST.get('value')

		if request.POST.get('id'):
			id=request.POST.get('id')
			obj = userinfo.objects.get(excelid=id)
			obj.present = not obj.present
			obj.save()
			d=[]
			data = {
			'dataset':d
			}
			return JsonResponse(data)



		if((searchby=="" or searchby==None) and (value=="Not Applicable" or value=="")):
			error1=True
		if((searchby=="phone no:" or searchby=="excelid") and value==""):
			error2=True
		if(searchby=="phone"):
			result=userinfo.objects.filter(phone=value)
			if(len(result)==0):
				result=paid_userinfo.objects.filter(phone=value)
			sb=0
		elif(searchby=="excelid"):
			result=userinfo.objects.filter(excelid=value)
			if(len(result)==0):
				result=paid_userinfo.objects.filter(excelid=value)
			sb=0
		elif(searchby=="name"):
			result=userinfo.objects.filter(name__icontains=value)
			obj=paid_userinfo.objects.filter(name__icontains=value)
			result = list(chain(result,obj))

			# if(len(result)==0):
			# 	result=paid_userinfo.objects.filter(name__icontains=value)
			sb=0

		context={
		"title":"testing",
		"searchby":searchby,
		"value":value,
		"error1":error1,
		"error2":error2,
		"searchby_num":sb,
		"obj":result,
		"len":len(result)
		}
		return render(request,"searchby.html",context)
