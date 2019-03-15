from django.db import models
from datetime import date,datetime
from slugger import AutoSlugField

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	book_url = models.URLField(max_length=150, blank=True, null=True)
	book_description = models.CharField(max_length=5000, blank=True, null=True)
	date_added = models.DateTimeField('date added', auto_now=True)
	
	#book_image = models.ImageField(upload_to=)
	#add favorited #TODO
	slugger= AutoSlugField(unique=True, populate_from="title", blank=True, null=True,)

	class Meta:
		ordering = ["-date_added"]

	def __str__(self):
		return self.title
	
class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	class Meta:
		ordering = ["last_name", "first_name"]

	def __str__(self):
		return f'{self.last_name}, {self.first_name}'