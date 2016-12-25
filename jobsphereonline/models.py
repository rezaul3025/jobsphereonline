from django.db import models
from django import forms

class Tag(models.Model):
	identifier = models.CharField(max_length=128)
	name = models.CharField(max_length=255)

class Location(models.Model):
	identifier = models.CharField(max_length=128)
	name = models.CharField(max_length=255)

class Category(models.Model):
	identifier = models.CharField(max_length=128)
	name = models.CharField(max_length=255)

class Job(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	createddate = models.DateTimeField(auto_now_add=True, blank=True)
	applicationoption = models.CharField(max_length=45)
	applicationurl = models.CharField(max_length=255)
	status = models.CharField(max_length=45)
	owner = models.CharField(max_length=45)
	category=models.ManyToManyField(Category)
	location=models.ManyToManyField(Location)
	tag=models.ManyToManyField(Tag)

class Employer(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	address = models.CharField(max_length=255)
	website = models.CharField(max_length=255)
	logo = models.FileField(upload_to='employer/logo/')
	email = models.CharField(max_length=255)