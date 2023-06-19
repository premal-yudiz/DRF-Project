from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)


    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        print("before update",instance.name)
        instance.name = validated_data.get('name', instance.name)
        print("after update",instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance

    
