from django.db import models


class dog(models.Model):
	name=models.CharField(max_length=1000,blank=False)
	gender=models.CharField(max_length=1000,blank=False)
	color=models.CharField(max_length=1000,blank=False)
	favoritefood=models.CharField(max_length=1000,blank=False)
	favoritetoy=models.CharField(max_length=1000,blank=False)
	
	def __str__(self):
		return str(self.name)

	def test():
		pass