# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from doggy.models import dog,  breed

# Register your models here.
class dogList(admin.ModelAdmin):
	list_display=('name','age','gender','color','favoritefood','favoritetoy')

class breedList(admin.ModelAdmin):
	list_display=('name','size','friendliness','trainability','sheddingAmount','exerciseneeds')


admin.site.register(breed,breedList)
admin.site.register(dog,dogList)