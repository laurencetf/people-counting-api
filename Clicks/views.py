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

class Clicks(views.APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "No request provided"}, status="400", headers= {"Access-Control-Allow-Origin": "*"})
        else:
            imageId = request.data['imageId']
            top = request.data['Top']
            left = request.data['Left']
            userId = request.data['userId']
            if Click.objects.filter(imageId=imageId, top=top, left=left).exists():
                resp = JsonResponse({'Error': "Click already processed"}, status="400")
            else:
                db_click = Click()
                db_click.imageId = imageId
                db_click.top = top
                db_click.left = left
                db_click.userId = userId
                db_click.save() 
                return JsonResponse({'Success': "Successfully added"}, status="200")
            resp['Access-Control-Allow-Origin'] = "*"
            return resp