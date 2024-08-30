from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import RegisterForm
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.db.models import Q
from .library import Pagination
from rest_framework.response import Response
import re

def register(response):
    if response.method=="POST":
        form = RegisterForm( response.POST)
        if form.is_valid():
            form.save()

    else:
        form =RegisterForm()
    return render(response,"register.html",{'form':form})

# Create your views here.
class SearchUser(APIView):
    def get(self,request):
        user_name = request.GET.get('user_name', None)
        page_no = int(request.GET.get('page', '1'))
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(regex, user_name):
            output = User.objects.filter(email=user_name)
        else:
            output = User.objects.filter(username__contains =user_name)
        ov = User.objects.filter(email=user_name).values()
        pagn = Pagination()
        results = {}
        result =[]
        res ={}
        pagn.get_offsets(page_no)
        user = output[0]

        res['username'] = user.username
        res['email_id'] = user.email
        res['is_active'] = user.is_active
        res['is_superuser'] = user.is_superuser
        result.append(res)
        results['user_data'] = result
        total_records = 1
        results['pagination'] = pagn.get_paginator(total_records)
        print(results)
        return Response(results, content_type="application/json")

