# -*- coding: utf 8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
	emitter = models.ForeignKey(User, related_name='+')
	receiver = models.ForeignKey(User)
	date_message = models.DateTimeField(default=timezone.now)
	text = models.TextField(verbose_name='Message')
	visualized = models.BooleanField(default=False)

	def __str__(self):
		return 'Message from ' + self.emitter.first_name + ' for ' + self.receiver.first_name

	def get_30_messages(self, user_loged, user_visited):
		ms = list()

		mlog = Message.objects.filter(emitter=user_loged, receiver=user_visited)
		mvis = Message.objects.filter(emitter=user_visited, receiver=user_loged)

		for m in mlog:ms.append(m)
		for m in mvis:
			if m.visualized == False:
				m.visualized = True
				m.save()
			ms.append(m)

		return sorted(ms, key=lambda inst: inst.date_message)[::-1][0:30][::-1]

	def format_date_chat(self, data):
		return self.less_than_10(data.day) + "/" + self.less_than_10(data.month) + "/" + str(data.year) + " at " + self.less_than_10(data.hour) + ":" + self.less_than_10(data.minute) + ":" + self.less_than_10(data.second)

	def less_than_10(self, n):
		if n < 10:
			return "0"+ str(n)
		return str(n)

	def get_all_messages(self, user_loged, user_visited):
		ms = list()

		mlog = Message.objects.filter(emitter=user_loged, receiver=user_visited)
		mvis = Message.objects.filter(emitter=user_visited, receiver=user_loged)

		for m in mlog:ms.append(m)
		for m in mvis:
			if m.visualized == False:
				m.visualized = True
				m.save()
			ms.append(m)

		lista =  sorted(ms, key=lambda inst: inst.date_message)

		json = []

		for msg in lista:
			if msg.emitter == user_loged:
				a = [0, msg.text, self.format_date_chat(msg.date_message)]
			else:
				a = [1, msg.text, self.format_date_chat(msg.date_message)]
			json.append(a)
		return json

	def get_messages_not_view(self, user_loged, user_visited):
		a = list()
		mvis = Message.objects.filter(emitter=user_visited, receiver=user_loged)

		for m in mvis:
			if m.visualized == False:
				a.append(([m.text], ["{}/{} - {}:{}:{}".format(m.date_message.month, m.date_message.day, m.date_message.hour, m.date_message.minute, m.date_message.second)]))
		return a

	def set_read_message(self, user_loged, user_visited):
		mvis = Message.objects.filter(emitter=user_visited, receiver=user_loged)
		for m in mvis:
			if m.visualized == False:
				m.visualized = True
				m.save()
		return True

	def send_message(self, user_loged, user_visited, message_text):
		newMessage = Message()
		newMessage.text = message_text
		newMessage.emitter = user_loged
		newMessage.receiver = user_visited
		newMessage.save()
		return[newMessage.text, self.format_date_chat(newMessage.date_message)]

	def check_read_ultimate_message(self, user_loged, user_visited):
		ms = list()

		mlog = Message.objects.filter(emitter=user_loged, receiver=user_visited)
		mvis = Message.objects.filter(emitter=user_visited, receiver=user_loged)

		for m in mlog:ms.append(m)
		for m in mvis:ms.append(m)

		if len(ms) == 0:return False

		ultimate_message = sorted(ms, key=lambda inst: inst.date_message)[-1]
		if ultimate_message.emitter == user_loged and ultimate_message.visualized == True:
			return True
		return False

	def delete_messages(self, user_loged, user_visited):
		Message.objects.filter(emitter=user_loged, receiver=user_visited).delete()
		Message.objects.filter(emitter=user_visited, receiver=user_loged).delete()
		return True