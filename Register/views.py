import django
from django.views.generic.edit import CreateView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import render

class Register(APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        email = request.data['email']
        password = request.data['password']
        color = request.data['color']
        if User.objects.filter(username=email).exists():
            return Response({'Error': "Already registered"}, status="400")
        else:
            user = User.objects.create_user(email,email, password)
            user.first_name = color
            user.last_name = color
            user.is_active = True
            user.is_staff = False
            user.is_superuser = False
            user.save()
            res = User.objects.get(username=email)
            return Response({'id':str(res.id), "email":res.email,"password":res.password,"color":res.first_name}, status=200)