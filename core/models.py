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
