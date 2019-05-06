import jwt,json
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import datetime
import time

class Authenticate(APIView):

    def converter(obj):
        if isinstance(obj, datetime.datetime):
            return obj.__str__()

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        email_r = request.data['email']
        password_r = request.data['password']
        user = authenticate(username=email_r, password=password_r)
        if user:
            expiry = datetime.date.today() + datetime.timedelta(days=7)
            token = jwt.encode({'id':user.id,'username': user.username, 'expiry':expiry.__str__()}, 'PCSK',  algorithm='HS256')    
            return HttpResponse(
              token,
              status=200,
              content_type="application/json"
            )
        else:
            return Response(
              json.dumps({'Error': "Invalid credentials"}),
              status=400,
              content_type="application/json"
            )