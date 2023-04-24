from django.contrib import admin
from .models import Employee , FingerprintIdentity, DailyAttendance

# Register your models here.
model_list = [Employee, FingerprintIdentity, DailyAttendance]
admin.site.register(model_list)

