from rest_framework import serializers
from doggy.models import dog, breed
class dogSerializer(serializers.Serializer):
 	id= serializers.IntegerField(read_only=True)
 	name=serializers.CharField(max_length=1000)
 	gender=serializers.CharField()
 	color=serializers.CharField()
	favoritefood=serializers.CharField()
	favoritetoy=serializers.CharField()

	def create(self, validated_data):
		return dog.objects.create(**validated_data) 	
 	def  update(self, instance,validated_data):
 		instance.name=validated_data.get('name',instance.name)
 		instance.age=validated_data.get('age',instance.age)
 		instance.gender=validated_data.get('gender',instance.gender)
 		instance.color=validated_data.get('color',instance.color)
 		instance.favoritefood=validated_data.get('favoritefood',instance.favoritefood)
 		instance.favoritetoy=validated_data.get('favoritetoy',instance.favoritetoy)
 		instance.save()
 		return instance


 