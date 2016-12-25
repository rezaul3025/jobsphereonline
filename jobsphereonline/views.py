from django.http import HttpResponse
from django.shortcuts import render,redirect, RequestContext,render_to_response
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import Http404,HttpRequest,HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods

from django.core import serializers

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from jobsphereonline.models import Tag,Location,Category,Job,Employer

from jobsphereonline.forms import EmployerForm

from django.db.models import Q

def index(request):
	#conn = getConnection()
	#categories = Category.objects.all()
	return render(request, 'index.html',{'category_list':''})

def createjob(request):
	return render(request, 'job/create.html')

def jobpostsuccess(request):
	return render(request, 'job/jobpostsuccess.html')

def empsignupsuccess(request):
	return render(request, 'employer/signsuccess.html')

def searchjob(request):
	searchKeyLocation = request.GET['location']
	searchKeyTag = request.GET['tag']
	page = request.GET['page']

	tags = Tag.objects.filter(name__icontains=searchKeyTag)
	locations = Location.objects.filter(name__icontains=searchKeyLocation)

	print(tags)
	if searchKeyLocation and searchKeyTag:
		job_list = Job.objects.filter(location__in=locations ,tag__in=tags)
	elif searchKeyTag:
		job_list = Job.objects.filter(tag__in=tags)
	elif searchKeyLocation:
		job_list = Job.objects.filter(location__in=locations )
	else:
		job_list = []

	paginator = Paginator(job_list, 5)
    
	try:
		jobs = paginator.page(page)
	except PageNotAnInteger:
		jobs = paginator.page(1)
	except EmptyPage:
		jobs = paginator.page(paginator.num_pages)

	return render(request, 'job/search.html',{'jobs':jobs,'searchKeyTag':searchKeyTag,'searchKeyLocation':searchKeyLocation})

def employersignup(request):
	if request.method == 'POST':
		form = EmployerForm(request.POST, request.FILES)
		#print(form.is_valid())
		if form.is_valid():
            # file is saved
			title = request.POST['title']
			email = request.POST['email']
			password = request.POST['password']
			description = request.POST['description']
			address=request.POST['address']
			website = request.POST['website']
			logo = request.FILES['logo']
			existing_employer = Employer.objects.filter(email = email).first()
			#print(existing_employer)
			if existing_employer is None:
				employer = Employer(title=title,description=description,address=address,website=website,logo=logo, email=email)
				employer.save()
				user = User.objects.create_user(username=email, password = password, email = email, first_name=title, last_name = title, is_superuser=True)
				return HttpResponseRedirect('/employer/signupsuccess/')
			else:
				return HttpResponseRedirect('/employer/signup/?info_exist=True')
	else:
		form = EmployerForm()
		return render(request, 'employer/signup.html', {'form': form})

def userauthentication(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email, password=password)
		if user is not None:
  			if user.is_active:
  				login(request, user)
  				# Redirect to a success page.
  				return  redirect('/') #render(request, 'index.html')
  			else:
  				#Return a 'disabled account' error message
  				return  redirect('/login/') #render(request, 'login.html')
		else:
  			#Return an 'invalid login' error message
  			return  redirect('/login/') #render(request, 'login.html') 
	else:
		return render(request, 'login.html')

def dologout(request):
	logout(request)
	# Redirect to a success page.
	return  redirect('/') #render(request, 'index.html')






