# -*- coding: utf 8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import User
import json

def index(request):
	if not request.user.is_authenticated():
		return render(request, 'core/login.html')
	else:
		return render(request, 'core/index.html')

def register(request):
	if request.method == 'POST':
		userInstance = User()
		userInstance.first_name = request.POST.get('name')
		userInstance.username = request.POST.get('username')
		passw = request.POST.get('password')
		userInstance.set_password(passw)
		userInstance.save()
		user = authenticate(username=userInstance.username, password=passw)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse(json.dumps(True), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")

def make_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse(json.dumps(True), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")