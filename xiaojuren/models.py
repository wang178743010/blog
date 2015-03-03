#coding:utf-8
from django.db import models

class index(models.Model):
	img = models.ImageField(upload_to="./img")

class logo(models.Model):
	log = models.ImageField(upload_to="./img")

class book(models.Model):
	title = models.CharField(max_length = 20)
	content = models.TextField()
	date = models.DateField(auto_now = True)
	img = models.ImageField(upload_to="./img")

class Image(models.Model):
	img = models.ImageField(upload_to="./img")
	name = models.CharField(max_length = 20)

class link(models.Model):
	title = models.CharField(max_length = 20)

class link2(models.Model):
	tail = models.CharField(max_length = 20)
	content = models.TextField()
	img = models.ImageField(upload_to="./img")

class link3(models.Model):
	head = models.CharField(max_length = 20)
	content = models.CharField(max_length = 30)

class link6(models.Model):
	img = models.ImageField(upload_to="./img")

class link7(models.Model):
	name = models.CharField(max_length = 20)

	title = models.CharField(max_length="64")
	content = models.TextField()
	img = models.ImageField(upload_to="./img")