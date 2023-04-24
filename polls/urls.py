# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 19:32:10 2023

@author: Maringire
"""

from django.urls import path

from . import views

urlpatterns = [
        path('', views.index , name='index'),
        path('list', views.EmployeeListView.as_view(), name = 'mylist'),
        path('upload', views.upload_data, name='upload' ),
        path('testPost', views.testPost, name ='testPost'),
        
        ]