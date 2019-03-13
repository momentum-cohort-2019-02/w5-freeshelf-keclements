from django.db import models

# Create your models here.

class Books(models.Models):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	

	def __str__(self):
		return self.name
	
	