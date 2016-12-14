# -*- coding: utf 8 -*-
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import User
from django.http import Http404
from .models import Message
import json

def index(request):
	if not request.user.is_authenticated():
		return render(request, 'core/login.html')
	else:
		instance_message = Message()
		recently_users = instance_message.get_users_recently(request.user)
		count_messages = instance_message.count_messages(request.user)
		all_users = sorted(User.objects.all(), key=lambda inst: inst.date_joined)[::-1]
		return render(request, 'core/index.html', {'recently_users':recently_users, 'all_users':all_users, 'count_messages':count_messages})

def register(request):
	if request.method == 'POST' and request.is_ajax():
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
	raise Http404

def make_login(request):
	if request.method == 'POST' and request.is_ajax():
		user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse(json.dumps(True), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404


def make_logout(request):
	if request.is_ajax():
		logout(request)
		return HttpResponse(json.dumps(True), content_type="application/json")
	raise Http404

def delete_account(request):
	if request.is_ajax():
		request.user.delete()
		return HttpResponse(json.dumps(True), content_type="application/json")
	raise Http404

def room(request, pkreceiver):
	if not request.user.is_authenticated():
		return render(request, 'core/login.html')
	else:
		instance_message = Message()
		user_visited = get_object_or_404(User, pk=pkreceiver)
		if request.user == user_visited:
			return render(request, 'core/alone.html')
		messages = instance_message.get_30_messages(request.user, user_visited)
		return render(request, 'core/room.html', {'messages':messages, 'user_visited':user_visited})

def about(request):
	return render(request, 'core/about.html')

# AJAX for the Chat room

def messages_not_view(request, pkreceiver):
	if not request.user.is_authenticated():
		return render(request, 'core/login.html')
	elif request.is_ajax():
		instance_message = Message()
		user_visited = get_object_or_404(User, pk=pkreceiver)
		if request.user == user_visited:
			return render(request, 'core/alone.html')
		messages = instance_message.get_messages_not_view(request.user, user_visited)
		print(messages)
		return HttpResponse(json.dumps(messages), content_type="application/json")
	raise Http404

def all_messages(request):
	if not request.user.is_authenticated():
		return render(request, 'core/login.html')
	else:
		if request.method == 'POST' and request.is_ajax():
			away = request.POST.get('id')
			instance_message = Message()
			user_visited = get_object_or_404(User, pk=away)
			if request.user == user_visited:
				return render(request, 'core/alone.html')
			result = instance_message.get_all_messages(request.user, user_visited)
			return HttpResponse(json.dumps(result), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def read_messages(request, pkreceiver):
	if not request.user.is_authenticated():
		return render(request, 'core/login.html')
	elif request.is_ajax():
		instance_message = Message()
		user_visited = get_object_or_404(User, pk=pkreceiver)
		if request.user == user_visited:
			return render(request, 'core/alone.html')
		result = instance_message.set_read_message(request.user, user_visited)
		return HttpResponse(json.dumps(result), content_type="application/json")
	raise Http404

def send_message(request, pkreceiver):
	if not request.user.is_authenticated():
		return render(request, 'core/login.html')
	else:
		if request.method == 'POST' and request.is_ajax():
			message = request.POST.get('id')
			print(message)
			instance_message = Message()
			user_visited = get_object_or_404(User, pk=pkreceiver)
			if request.user == user_visited:
				return render(request, 'core/alone.html')
			result = instance_message.send_message(request.user, user_visited, message)
			return HttpResponse(json.dumps(result), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def verify_read(request):
	if not request.user.is_authenticated():
		return render(request, 'core/login.html')
	else:
		if request.method == 'POST' and request.is_ajax():
			idvi = request.POST.get('id')
			instance_message = Message()
			user_visited = get_object_or_404(User, pk=idvi)
			if request.user == user_visited:
				return render(request, 'core/alone.html')
			result = instance_message.check_read_ultimate_message(request.user, user_visited)
			return HttpResponse(json.dumps(result), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def delete_chat(request):
	if not request.user.is_authenticated():
		return render(request, 'core/login.html')
	else:
		if request.method == 'POST' and request.is_ajax():
			idvi = request.POST.get('id')
			instance_message = Message()
			user_visited = get_object_or_404(User, pk=idvi)
			if request.user == user_visited:
				return render(request, 'core/alone.html')
			result = instance_message.delete_messages(request.user, user_visited)
			return HttpResponse(json.dumps(result), content_type="application/json")
		raise Http404
