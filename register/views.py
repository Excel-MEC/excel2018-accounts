from django.shortcuts import render
from django.views.generic import TemplateView
from register.forms import RegistrationForm, PaidRegistrationForm
import string

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