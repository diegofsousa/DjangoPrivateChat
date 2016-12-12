# -*- coding: utf 8 -*-
from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register),
    url(r'^login/$', views.make_login),
    url(r'^logout/$', views.make_logout),

    #Pages of inbox
    url(r'^message/(?P<pkreceiver>[0-9]+)/$', views.room, name='room'),

    #AJAX for Chat room
    url(r'^message/(?P<pkreceiver>[0-9]+)/newmessages/$', views.messages_not_view, name='messages_not_view'),
    url(r'^message/(?P<pkreceiver>[0-9]+)/read/$', views.read_messages, name='read_messages'),
    url(r'^message/(?P<pkreceiver>[0-9]+)/send/$', views.send_message, name='send_message'),
    url(r'^allmessages/$', views.all_messages, name='all_messages'),
    url(r'^verifyread/$', views.verify_read, name='verify_read'),
    url(r'^deletechat/$', views.delete_chat, name='delete_chat'),
]