from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
#from .forms import NewsForm, NewsModifyForm
from .models import Groups, Users, UserGroups
from django.utils import timezone
import random   
import string  
import secrets  
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import GroupsSerializer
from django.core import serializers
import uuid

@csrf_exempt
def add_user_to_group(request, randomstring):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        link = f"http://127.0.0.1/pai/joinmygroup/{randomstring}"
        group = get_object_or_404(Groups, Link=link)
        user = get_object_or_404(Users, UserGuid=data['user_uuid'])
        print(UserGroups.objects.filter(UserId=user, GroupId=group))
        if not UserGroups.objects.filter(UserId=user, GroupId=group):
            usergroup = UserGroups(UserId=user, GroupId=group)
            usergroup.save()
            return JsonResponse({
            "response": f"You have successfully joined group {group.Name}!"
            })
        return JsonResponse({
            "response": "You have already joined this group!"
        })


def get_group_link(request, group_uuid):
    if request.method == 'GET':
        group = get_object_or_404(Groups, GroupGuid=uuid.UUID(group_uuid))
        num = 10
        randomstring = "".join(secrets.choice(string.ascii_letters) for x in range(num))
        link = f"http://127.0.0.1/pai/joinmygroup/{randomstring}"
        # while(not Groups.objects.filter(Link=link)):
        #     randomstring = "".join(secrets.choice(string.ascii_letters) for x in range(num))
        #     link = f"http://127.0.0.1/pai/joinmygroup/{randomstring}"
        print(link)
        group.Link = link
        group.save()
        serializer = GroupsSerializer(group, many=False)
        return JsonResponse(serializer.data, safe=False)




