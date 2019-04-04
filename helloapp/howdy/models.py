from django.db import models
from django.urls import reverse


class Person(models.Model):
	name = models.CharField(max_length=200)
	datestamp = models.DateTimeField(auto_now_add=True)
	description = models.TextField(max_length=200, blank=True, null=True)
	image = models.FileField(blank=True, upload_to='uploads/')
	
	def __str__(self):
		return self.name

