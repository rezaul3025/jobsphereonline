from django.http import HttpResponse
from django.shortcuts import render,redirect, RequestContext,render_to_response
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import Http404,HttpRequest,HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods

from django.core import serializers

import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from jobsphereonline.models import Tag,Location,Category,Job

from django.db.models import Q


@require_http_methods(["GET"])
def searchtags(request):
	searchKey = request.GET['searchKey']
	print(searchKey)
	tags = Tag.objects.filter(name__icontains=searchKey)
	data = serializers.serialize('json', tags,fields=('name'))
	print(data)
	
	return HttpResponse(data, content_type="application/json")

def gettags(request):
	selected = request.GET['selected']
	query = request.GET['query']
	page = request.GET['page']
	pageSize = request.GET['pageSize']

	if query:
		tag_list = Tag.objects.filter(name__icontains=query).exclude(name=selected)
	else:
		tag_list = Tag.objects.all()

	paginator = Paginator(tag_list, pageSize)

	try:
		tags = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		tags = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		tags = paginator.page(paginator.num_pages)

	data = serializers.serialize('json', tags,fields=('name'))
	print(data)
	
	return HttpResponse(data, content_type="application/json")


@require_http_methods(["GET"])
def searchlocations(request):
	searchKey = request.GET['searchKey']
	print(searchKey)
	locations = Location.objects.filter(name__icontains=searchKey)
	data = serializers.serialize('json', locations,fields=('name'))
	print(data)
	
	return HttpResponse(data, content_type="application/json")

@require_http_methods(["GET"])
def getlocations(request):
	selected = request.GET['selected']
	query = request.GET['query']
	page = request.GET['page']
	pageSize = request.GET['pageSize']

	if query:
		location_list = Location.objects.filter(name__icontains=query).exclude(name=selected)
	else:
		location_list = Location.objects.all()

	paginator = Paginator(location_list, pageSize)

	try:
		locations = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		locations = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		locations = paginator.page(paginator.num_pages)

	data = serializers.serialize('json', locations,fields=('name'))
	print(data)
	
	return HttpResponse(data, content_type="application/json")

@require_http_methods(["GET"])
def getcategory(request):
	selected = request.GET['selected']
	query = request.GET['query']
	page = request.GET['page']
	pageSize = request.GET['pageSize']

	if query:
		category_list = Category.objects.filter(name__icontains=query).exclude(name=selected)
	else:
		category_list = Category.objects.all()

	paginator = Paginator(category_list, pageSize)

	try:
		categories = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		categories = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		categories = paginator.page(paginator.num_pages)

	data = serializers.serialize('json', categories,fields=('name'))
	print(data)
	
	return HttpResponse(data, content_type="application/json")

@require_http_methods(["POST"])
@csrf_exempt
def postjob(request):
	title = request.POST['title']
	description = request.POST['description']
	applicationoption = request.POST['applicationoption']
	applicationurl = request.POST['applicationurl']
	category = request.POST['category']
	location = request.POST['location']
	tag = request.POST['tag']
	job = Job(title=title,description=description,applicationoption=applicationoption,applicationurl=applicationurl,status='published',owner='test')
	
	job.save()
	category=category.split(",")
	#print(category)
	location = location.split(",")
	tag = tag.split(",")
	categories = Category.objects.filter(name__in=category)
	locations = Location.objects.filter(name__in=location)
	tags = Tag.objects.filter(name__in=tag)
	#print(categories)
	for categoryOb in categories:
		job.category.add(categoryOb)
	for locationOb in locations:
		job.location.add(locationOb)
	for tagOb in tags:
		job.tag.add(tagOb)

	data = serializers.serialize('json', [job],fields=('title'))
	print(data)
	
	return HttpResponse(data)







