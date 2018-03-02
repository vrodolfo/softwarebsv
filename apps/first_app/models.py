# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.
class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(str(postData['first_name'])) < 2 or len(str(postData['first_name'])) > 255:
			errors['first_name'] = "First name should be more than 2 characters and less than 255."
		if any(map(str.isdigit, str(postData['first_name']))):
			errors['first_name'] = "First name should be letters only"

		if len(str(postData['last_name'])) < 2 or len(str(postData['last_name'])) > 255:
			errors['last_name'] = "Last name should be more than 2 characters"
		if any(map(str.isdigit, str(postData['last_name']))):
			errors['last_name'] = "Last name should be letters only"

		if not EMAIL_REGEX.match(str(postData['email_address'])):
			errors['email_address'] = "Invalid Email Format"

		duplicate = Users.objects.filter(email_address=postData['email_address']).first()
		if duplicate:
			errors['email_address'] = "Email already exist!"

		if len(str(postData['password'])) < 8:
			errors['password'] = "Password should be more than 8 characters"
		elif not any(map(str.isupper, str(postData['password']))):
			errors['password'] = "Password should contain at least 1 Capital Letter"

		#validations for birthdate
		
		return errors


class Users(models.Model):
	first_name    = models.CharField(max_length=255)
	last_name     = models.CharField(max_length=255)
	usertype      = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)
	password      = models.CharField(max_length=255)
	created_at    = models.DateTimeField(auto_now_add = True)
	updated_at    = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __unicode__(self):
		return "id: " + str(self.id) + "first_name: " + str(self.first_name) + ", last_name: " + str(self.last_name) +  "email_address: " + str(self.email_address) +  "password: " + str(self.password)

"""
models come with a hidden key:
      objects = models.Manager()
we are going to overwrite this!
"""


class Companies(models.Model):
	name       = models.CharField(max_length=255)
	shortdesc  = models.CharField(max_length=255)
	phone1     = models.CharField(max_length=255)
	phone2     = models.CharField(max_length=255)
	phone3     = models.CharField(max_length=255)
	email      = models.CharField(max_length=255)
	about_spanish      = models.TextField(max_length=1000)
	about_english      = models.TextField(max_length=1000)
	address1      = models.CharField(max_length=255)
	address2      = models.CharField(max_length=255)
	created_at    = models.DateTimeField(auto_now_add = True)
	updated_at    = models.DateTimeField(auto_now=True)
	# objects = CompanyManager()

	def __unicode__(self):
		return "id: " + str(self.id) + "name: " + str(self.name) + ", shortdesc: " + str(self.shortdesc) +  "phone1: " + str(self.phone1) +  "phone2: " + str(self.phone2)+  "phone3: " + str(self.phone3) +  "email: " + str(self.email)+  "address1: " + str(self.address1)+  "address2: " + str(self.address2) +  "about_english: " + str(self.about_english) +  "about_spanish: " + str(self.about_spanish)



class ServiceManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(str(postData['serviceName'].encode('utf-8'))) < 2:
			errors['serviceName'] = "El nombre debe ser de al menos 5 caracteres."
		if len(str(postData['serviceNameS'].encode('utf-8'))) < 2:
			errors['serviceNameS'] = "El nombre del Slider debe ser de al menos 5 caracteres."
		if len(str(postData['content1'].encode('utf-8'))) < 2:
			errors['content1'] = "El contenido del menu debe ser de al menos 5 caracteres."
		if len(str(postData['serviceName'].encode('utf-8'))) > 255:
			errors['serviceName'] = "Name should be less than 255 characters"
		if len(str(postData['serviceNameS'].encode('utf-8'))) > 255:
			errors['serviceNameS'] = "NameShort should be less than 255 characters"
		if len(str(postData['content1'].encode('utf-8'))) > 1000:
			errors['content1'] = "content1 should be less than 1000 characters"
		if len(str(postData['content2'].encode('utf-8'))) > 1000:
			errors['content2'] = "content2 should be less than 1000 characters"
		# if len(str(postData['content3'].encode('utf-8'))) > 1000:
		# 	errors['content3'] = "content3 should be less than 1000 characters"
		# if len(str(postData['content4'].encode('utf-8'))) > 1000:
		# 	errors['content4'] = "content4 should be less than 1000 characters"
		if len(str(postData['imageSlider'].encode('utf-8'))) > 255:
			errors['imageSlider'] = "imageSlider should be less than 255 characters"
		if len(str(postData['imageMenu'].encode('utf-8'))) > 255:
			errors['imageMenu'] = "imageMenu should be less than 255 characters"
		if len(str(postData['imageDetails1'].encode('utf-8'))) > 255:
			errors['imageDetails1'] = "imageDetails1 should be less than 255 characters"
		if len(str(postData['imageDetails2'].encode('utf-8'))) > 255:
			errors['imageDetails2'] = "imageDetails2 should be less than 255 characters"
		if len(str(postData['imageDetails3'].encode('utf-8'))) > 255:
			errors['imageDetails3'] = "imageDetails3 should be less than 255 characters"
		if len(str(postData['language'].encode('utf-8'))) > 255:
			errors['language'] = "language should be less than 255 characters"
		
		# duplicate = Services.objects.filter(serviceName=postData['serviceName']).first()
		# if duplicate:
		# 	errors['serviceName'] = "El Servicio ya existe"
		return errors



class Services(models.Model):
	company       = models.ForeignKey(Companies, related_name="services")
	serviceName   = models.CharField(max_length=255)
	serviceNameS  = models.CharField(max_length=255)
	content1      = models.TextField(max_length=1000)
	content2      = models.TextField(max_length=1000,null=True)
	content3      = models.TextField(max_length=1000,null=True)
	content4      = models.TextField(max_length=1000,null=True)
	position      = models.IntegerField(default=1)
	linkstatus    = models.BooleanField(default=False)
	active        = models.BooleanField(default=True)
	imageSlider   = models.CharField(max_length=255,null=True)
	imageMenu     = models.CharField(max_length=255,null=True)
	imageDetails1 = models.CharField(max_length=255,null=True)
	imageDetails2 = models.CharField(max_length=255,null=True)
	imageDetails3 = models.CharField(max_length=255,null=True)
	language      = models.CharField(max_length=255,default="spanish")
	created_at    = models.DateTimeField(auto_now_add = True)
	updated_at    = models.DateTimeField(auto_now=True)
	objects = ServiceManager()

	def __unicode__(self):
		return "id: " + str(self.id) + "company: " + str(self.company) + ", serviceName: " + str(self.serviceName) +  "serviceNameS: " + str(self.serviceNameS) +  "imageSlider: " + str(self.imageSlider)+  "imageMenu: " + str(self.imageMenu) +  "imageDetails1: " + str(self.imageDetails1)+  "imageDetails2: " + str(self.imageDetails2)+  "imageDetails3: " + str(self.imageDetails3) +  "content1: " + str(self.content1) +  "content2: " + str(self.content2) 


class ClientManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(str(postData['name'].encode('utf-8'))) < 2:
			errors['name'] = "El nombre debe ser de al menos 5 caracteres."
		if len(str(postData['nameShort'].encode('utf-8'))) < 2:
			errors['nameShort'] = "El nombre del Slider debe ser de al menos 5 caracteres."
		if len(str(postData['content1'].encode('utf-8'))) < 2:
			errors['content1'] = "El contenido del menu debe ser de al menos 5 caracteres."
		if len(str(postData['name'].encode('utf-8'))) > 255:
			errors['name'] = "name should be less than 255 characters"
		if len(str(postData['nameShort'].encode('utf-8'))) > 255:
			errors['nameShort'] = "nameShort should be less than 255 characters"
		if len(str(postData['nameLarge'].encode('utf-8'))) > 255:
			errors['nameLarge'] = "nameLarge should be less than 255 characters"
		if len(str(postData['content1'].encode('utf-8'))) > 5000:
			errors['content1'] = "content1 should be less than 5000 characters"
		if len(str(postData['content2'].encode('utf-8'))) > 5000:
			errors['content2'] = "content2 should be less than 5000 characters"
		# if len(str(postData['content3'].encode('utf-8'))) > 5000:
		# 	errors['content3'] = "content3 should be less than 5000 characters"
		# if len(str(postData['content4'].encode('utf-8'))) > 5000:
		# 	errors['content4'] = "content4 should be less than 5000 characters"
		if len(str(postData['imageSlider'].encode('utf-8'))) > 255:
			errors['imageSlider'] = "imageSlider should be less than 255 characters"
		if len(str(postData['imageMenu'].encode('utf-8'))) > 255:
			errors['imageMenu'] = "imageMenu should be less than 255 characters"
		if len(str(postData['imageDetails1'].encode('utf-8'))) > 255:
			errors['imageDetails1'] = "imageDetails1 should be less than 255 characters"
		if len(str(postData['imageDetails2'].encode('utf-8'))) > 255:
			errors['imageDetails2'] = "imageDetails2 should be less than 255 characters"
		if len(str(postData['imageDetails3'].encode('utf-8'))) > 255:
			errors['imageDetails3'] = "imageDetails3 should be less than 255 characters"
		if len(str(postData['website'].encode('utf-8'))) > 255:
			errors['website'] = "website should be less than 255 characters"
		if len(str(postData['language'].encode('utf-8'))) > 255:
			errors['language'] = "language should be less than 255 characters"

		# duplicate = Clients.objects.filter(name=postData['name']).first()
		# if duplicate:
		# 	errors['name'] = "El Cliente ya existe"
		return errors


class Clients(models.Model):
	company       = models.ForeignKey(Companies, related_name="clients")
	name          = models.CharField(max_length=255)
	nameShort     = models.CharField(max_length=255)
	nameLarge     = models.CharField(max_length=255)
	content1      = models.TextField(max_length=5000)
	content2      = models.TextField(max_length=5000,null=True)
	content3      = models.TextField(max_length=5000,null=True)
	content4      = models.TextField(max_length=5000,null=True)
	position      = models.IntegerField(default=1)
	linkstatus    = models.BooleanField(default=False)
	active        = models.BooleanField(default=True)
	imageSlider   = models.CharField(max_length=255,null=True)
	imageMenu     = models.CharField(max_length=255,null=True)
	imageDetails1 = models.CharField(max_length=255,null=True)
	imageDetails2 = models.CharField(max_length=255,null=True)
	imageDetails3 = models.CharField(max_length=255,null=True)
	website       = models.CharField(max_length=255,null=True)
	language      = models.CharField(max_length=255,default="spanish")
	created_at    = models.DateTimeField(auto_now_add = True)
	updated_at    = models.DateTimeField(auto_now=True)
	objects = ClientManager()

	def __unicode__(self):
		return "id: " + str(self.id) + ", company: " + str(self.company) +", name: " + str(self.name)+", nameShort: " + str(self.nameShort)+", nameLarge: " + str(self.nameLarge)+", content1: " + str(self.content1)+", content2: " + str(self.content2)+", content3: " + str(self.content3)+", position: " + str(self.position)+", linkstatus: " + str(self.linkstatus)+", active: " + str(self.active)+", imageSlider: " + str(self.imageSlider)+", imageMenu: " + str(self.imageMenu)+", imageDetails1: " + str(self.imageDetails1)+", imageDetails2: " + str(self.imageDetails2)+", imageDetails3: " + str(self.imageDetails3)+", website: " + str(self.website)+", language: " + str(self.language)

class ProjectManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if str(postData['client'].encode('utf-8')) == "":
			errors['client'] = "Debe asociar el proyecto a un cliente."
		if len(str(postData['name'].encode('utf-8'))) < 2:
			errors['name'] = "El nombre debe ser de al menos 5 caracteres."
		if len(str(postData['descShort'].encode('utf-8'))) < 2:
			errors['descShort'] = "El contenido del menu debe ser de al menos 5 caracteres."
		if len(str(postData['projectsStatus'].encode('utf-8'))) > 255:
			errors['projectsStatus'] = "projectsStatus should be less than 255 characters"
		if len(str(postData['name'].encode('utf-8'))) > 255:
			errors['name'] = "name should be less than 255 characters"
		if len(str(postData['nameShort'].encode('utf-8'))) > 255:
			errors['nameShort'] = "nameShort should be less than 255 characters"
		if len(str(postData['nameLarge'].encode('utf-8'))) > 255:
			errors['nameLarge'] = "nameLarge should be less than 255 characters"
		if len(str(postData['descShort'].encode('utf-8'))) > 255:
			errors['descShort'] = "descShort should be less than 255 characters"
		if len(str(postData['descLong'].encode('utf-8'))) > 5000:
			errors['descLong'] = "descLong should be less than 5000 characters"
		if len(str(postData['platform'].encode('utf-8'))) > 5000:
			errors['platform'] = "platform should be less than 5000 characters"
		if len(str(postData['technologies'].encode('utf-8'))) > 5000:
			errors['technologies'] = "technologies should be less than 5000 characters"
		# if len(str(postData['content'].encode('utf-8'))) > 5000:
		# 	errors['content'] = "content should be less than 5000 characters"
		if len(str(postData['imageSlider'].encode('utf-8'))) > 255:
			errors['imageSlider'] = "imageSlider should be less than 255 characters"
		if len(str(postData['imageMenu'].encode('utf-8'))) > 255:
			errors['imageMenu'] = "imageMenu should be less than 255 characters"
		if len(str(postData['imageDetails1'].encode('utf-8'))) > 255:
			errors['imageDetails1'] = "imageDetails1 should be less than 255 characters"
		if len(str(postData['imageDetails2'].encode('utf-8'))) > 255:
			errors['imageDetails2'] = "imageDetails2 should be less than 255 characters"
		if len(str(postData['imageDetails3'].encode('utf-8'))) > 255:
			errors['imageDetails3'] = "imageDetails3 should be less than 255 characters"
		# if len(str(postData['website'].encode('utf-8'))) > 255:
		# 	errors['website'] = "website should be less than 255 characters"
		if len(str(postData['language'].encode('utf-8'))) > 255:
			errors['language'] = "language should be less than 255 characters"

		# duplicate = Clients.objects.filter(name=postData['name']).first()
		# if duplicate:
		# 	errors['name'] = "El Cliente ya existe"
		return errors


class Projects(models.Model):
	company        = models.ForeignKey(Companies, related_name="companyprojects")
	client         = models.ForeignKey(Clients, related_name="clientprojects")
	projectsStatus = models.CharField(max_length=255)
	name          = models.CharField(max_length=255)
	nameShort     = models.CharField(max_length=255)
	nameLarge     = models.CharField(max_length=255)
	descShort     = models.TextField(max_length=255)
	descLong      = models.TextField(max_length=5000,null=True)
	platform      = models.TextField(max_length=5000,null=True)
	technologies  = models.TextField(max_length=5000,null=True)
	content       = models.TextField(max_length=5000,null=True)
	position      = models.IntegerField(default=1)
	hours         = models.IntegerField(default=1)
	teamsize      = models.IntegerField(default=1)
	linkstatus    = models.BooleanField(default=False)
	active        = models.BooleanField(default=True)
	featured      = models.BooleanField(default=True)
	imageSlider   = models.CharField(max_length=255,null=True)
	imageMenu     = models.CharField(max_length=255,null=True)
	imageDetails1 = models.CharField(max_length=255,null=True)
	imageDetails2 = models.CharField(max_length=255,null=True)
	imageDetails3 = models.CharField(max_length=255,null=True)
	website       = models.CharField(max_length=255,null=True)
	language      = models.CharField(max_length=255,default="spanish")
	created_at    = models.DateTimeField(auto_now_add = True)
	updated_at    = models.DateTimeField(auto_now=True)
	objects = ProjectManager()

		
	def __unicode__(self):
		return "id: " + str(self.id) + ", company: " + str(self.company)+ ", client: " + str(self.client)+ ", projectsStatus: " + str(self.projectsStatus)+ ", name: " + str(self.name)+ ", nameShort: " + str(self.nameShort)+ ", nameLarge: " + str(self.nameLarge)+ ", descShort: " + str(self.descShort)+ ", descLong: " + str(self.descLong)+ ", platform: " + str(self.platform)+ ", technologies: " + str(self.technologies)+ ", position: " + str(self.position)+ ", hours: " + str(self.hours)+ ", teamsize: " + str(self.teamsize)+ ", linkstatus: " + str(self.linkstatus)+ ", active: " + str(self.active)+ ", featured: " + str(self.featured)+ ", imageSlider: " + str(self.imageSlider)+ ", imageMenu: " + str(self.imageMenu)+ ", imageDetails1: " + str(self.imageDetails1)+ ", imageDetails2: " + str(self.imageDetails2)+ ", imageDetails3: " + str(self.imageDetails3)+ ", website: " + str(self.website)+ ", language: " + str(self.language)


		