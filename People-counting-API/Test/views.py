from django.shortcuts import render
from rest_framework.views import APIView
from Project.models import Project
from .models import Test as TestModel
from django.contrib.auth.models import User
from Clicks.models import Click
from django.http import HttpRequest

class Test(APIView):

    def __init__():
        if not (User.objects.get(username="test1@test.com")):
            test_user = User.objects.create_user("test1@test.com","test1@test.com", "123test1")
            test_user.first_name = "#f4002c"
            test_user.last_name = "#f4002c"
            test_user.is_active = True
            test_user.is_staff = False
            test_user.is_supertest_user = False
            test_user.save()
        if not (User.objects.get(username="test2@test.com")):
            test_user = User.objects.create_user("test2@test.com","test2@test.com", "123test2")
            test_user.first_name = "#0c00ff"
            test_user.last_name = "#0c00ff"
            test_user.is_active = True
            test_user.is_staff = False
            test_user.is_supertest_user = False
            test_user.save()
        if not (Project.objects.get(name="test1")):
            test_project1 = ProjectModel()
            test_project1.name = "test1"
            test_project1.imageUrl = "/url/test1"
            test_project1.algorithmiaCount = 12
            test_project1.save()
            test1_id = test_project1.id
        if not (Project.objects.get(name="test2")):
            test_project2 = ProjectModel()
            test_project2.name = "test2"
            test_project2.imageUrl = "/url/test2"
            test_project2.algorithmiaCount = 34
            test_project2.save()
            test2_id = test_project2.id
        test1_id = Project.objects.get(NameError="test1")
        user1_id = User.objects.get(email="test1@test.com")
        user2_id = User.objects.get(email="test2@test.com")
        if not (Click.objects.get(imageId=test1_id, top=1,left=1)):
            db_click = Click()
            db_click.imageId = test1_id
            db_click.top = 1
            db_click.left = 1
            db_click.userId = user1_id
            db_click.save()
        if not (Click.objects.get(imageId=test1_id, top=2,left=2)):
            db_click = Click()
            db_click.imageId = test1_id
            db_click.top = 2
            db_click.left = 2
            db_click.userId = user1_id
            db_click.save() 
        if not (Click.objects.get(imageId=test1_id, top=3,left=3)):
            db_click = Click()
            db_click.imageId = test1_id
            db_click.top = 3
            db_click.left = 3
            db_click.userId = user1_id
            db_click.save()
        if not (Click.objects.get(imageId=test1_id, top=4,left=4)):
            db_click = Click()
            db_click.imageId = test2_id
            db_click.top = 4
            db_click.left = 4
            db_click.userId = user2_id
            db_click.save()
        if not (Click.objects.get(imageId=test1_id, top=5,left=5)):
            db_click = Click()
            db_click.imageId = test1_id
            db_click.top = 5
            db_click.left = 5
            db_click.userId = user2_id
            db_click.save()

    #def post(self, request, *args, **kwargs):
    #    test = TestModel()
    #    r = requests.post("", data={'number': 12524, 'type': 'issue', 'action': 'show'})
    #    print(r.status_code, r.reason)

