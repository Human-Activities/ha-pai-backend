from rest_framework import serializers
from pai.models import Groups, UserGroups
import random   
import string  
import secrets
from django.shortcuts import render, redirect, get_object_or_404

class GroupsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Name = serializers.CharField()
    Description = serializers.CharField()
    Link = serializers.CharField()

    def create(self, validated_data):
        return Groups.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.Name = validated_data.get('name', instance.Name)
        instance.Description = validated_data.get('description', instance.Description)
        instance.Link = validated_data.get('link', instance.Link)
        # group = get_object_or_404(Groups, id=instance.group_id)
        # num = 10
        # link = f"https://activities.join/".join(secrets.choice(string.ascii_letters) for x in range(num))
        # while(Groups.objects.filter(link=link) is not None):
        #     link = f"https://activities.join/".join(secrets.choice(string.ascii_letters) for x in range(num))
        # group.link = link
        # group.save()
        instance.save()
        return instance