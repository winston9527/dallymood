import json

from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.forms.models import model_to_dict

from users.models import Users


def register(request):
    data = json.loads(request.body)
    try:
        user = Users.objects.create(**data)
        user = model_to_dict(user)
        return JsonResponse({'code': 201, 'message': 'created', 'data': user}, status=201)
    except IntegrityError:
        return JsonResponse({'code': 400, 'message': '身份证号码已存在！'}, status=200)


def login(request):
    data = json.loads(request.body)
    print(data)
    try:
        user = Users.objects.create(**data)
        user = model_to_dict(user)
        return JsonResponse({'code': 201, 'message': 'created', 'data': user}, status=201)
    except IntegrityError:
        return JsonResponse({'code': 400, 'message': '身份证号码已存在！'}, status=200)


def get(self, request):
    data = json.loads(request.body) if request.body else {}
    users = list(Users.objects.filter(**data).all().values())
    return JsonResponse({"list": users})
