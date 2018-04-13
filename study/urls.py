#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from study import views


urlpatterns = [
    url(r'^test/$', views.test, name="test"),
]