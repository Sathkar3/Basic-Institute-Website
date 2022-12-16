from django.shortcuts import render
from app1.forms import ContactForm
from app1.models import Employee

# Create your views here.


def homeview(request):
	return render(request,'app1/home.html')


def aboutview(request):
	return render(request,'app1/about.html')  


def servicesview(request):
	return render(request,'app1/services.html')


def galleryview(request):
	return render(request,'app1/gallery.html')  


def contactview(request):
	form=ContactForm()
	if request.method=="POST":
		form=ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return successview(request)
	return render(request,'app1/contact.html',{'f':form})

def successview(request):
	return HttpResponse('<h1>Successfull...!!!</h1>')


def usersview(request):
	employee = Employee.objects.all()
	return render(request,'app1/users.html',{'e':employee})





