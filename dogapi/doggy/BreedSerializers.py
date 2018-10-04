from rest_framework import serializers
from doggy.models import dog, breed



class breedSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    exerciseneeds=serializers.IntegerField()
    sheddingAmount=serializers.IntegerField()
    name=serializers.CharField()
    size=serializers.CharField()
    friendliness=serializers.IntegerField()
    trainability=serializers.IntegerField()

    def create(self, validated_data):
	    return breed.objects.create(**validated_data)
    def  update(self, instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.exerciseneeds=validated_data.get('exerciseneeds',instance.exerciseneeds)
        instance.sheddingAmount=validated_data.get('sheddingAmount',instance.sheddingAmount)
        instance.size=validated_data.get('size',instance.size)
        instance.friendliness=validated_data.get('friendliness',instance.friendliness)
        instance.trainability=validated_data.get('trainability',instance.trainability)
        instance.save()
        return instance
