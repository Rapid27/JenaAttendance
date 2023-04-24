# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:10:19 2023

@author: Maringire
"""
from polls.models import Employee

l1 = Employee.objects.order_by("pub_date")[0]

print(l1)