# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class breed(models.Model):
	"""docstring for ClassName"""
	dogsize=[('Tiny','Tiny'),('Small','Small'),('Medium','Medium'),('Large','Large')]
	dogfriendlychoice=[(1,1),(2,2),(3,3),(4,4),(5,5)]
	# trainabilitychoice=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
	exerciseneeds=models.IntegerField(choices=dogfriendlychoice,default=1)
	sheddingAmount=models.IntegerField(choices=dogfriendlychoice,default=1)
	name=models.CharField( max_length=1000,blank=False)
	size=models.CharField(choices=dogsize,max_length=1000)
	friendliness=models.IntegerField(choices=dogfriendlychoice)
	trainability=models.IntegerField(choices=dogfriendlychoice)
   	def __str__(self):
		return str(self.name)
		

class dog(models.Model):
	
	name=models.CharField(max_length=1000,blank=False)
	age=models.IntegerField(blank=False,default=5)
	breed=models.ForeignKey(breed,on_delete=models.CASCADE)
	gender=models.CharField(max_length=1000,blank=False)
	color=models.CharField(max_length=1000,blank=False)
	favoritefood=models.CharField(max_length=1000,blank=False)
	favoritetoy=models.CharField(max_length=1000,blank=False)
	
	def __str__(self):
		return str(self.name)