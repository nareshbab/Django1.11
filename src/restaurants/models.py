from django.db import models

# Create your models here.

class Restaurant(models.Model):
	name = models.CharField(max_length=120)
	location = models.CharField(max_length=120, null=True, blank=True)
	category = models.CharField(max_length=120, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name



