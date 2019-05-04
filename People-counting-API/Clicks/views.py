from django.shortcuts import render
import django
import pathlib
from .models import Click
import os
from django.core import serializers
from rest_framework import views
from rest_framework.response import Response
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.contrib.auth.models import User
from .clickSerializer import ClickEncoder

class Clicks(views.APIView):

    def get(self, request, image_Id, *args, **kwargs):
        clicks = Click.objects.filter(imageId = image_Id).order_by('userId')
        userIds = clicks.values('userId').distinct()
        data =[]
        for userId in userIds:
            user_Id =userId['userId']
            user = User.objects.get(id = user_Id)
            user_clicks = list(clicks.filter(userId=user_Id))
            tmp_clicks = []
            for click in user_clicks:
                tmp_clicks.append({"Top": str(click.top),"Left": str(click.left)})
            tmp = {"userId": str(user_Id), "email": user.email, "color": user.first_name,"clicks": tmp_clicks}
            data.append(tmp)
        return JsonResponse(data, safe = False)


    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "No request provided"}, status="400")
        else:
            imageId = request.data['imageId']
            top = request.data['Top']
            left = request.data['Left']
            userId = request.data['userId']
            if Click.objects.filter(imageId=imageId, top=top, left=left).exists():
                return Response({'Error': "Click already processed"}, status="400")
            else:
                db_click = Click()
                db_click.imageId = imageId
                db_click.top = top
                db_click.left = left
                db_click.userId = userId
                db_click.save() 
                return Response({'Success': "Successfully added"}, status="200")
