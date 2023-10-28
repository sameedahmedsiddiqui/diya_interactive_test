from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('i_patient', 'i_counsellor', 'appointment_date')
    list_filter = ('appointment_date', 'is_active')


@admin.register(Counsellor)
class CounsellorAdmin(admin.ModelAdmin):

    list_filter = ('i_auth_user__is_active','i_auth_user__email')
    list_display = ['email', 'username', 'is_active']

    def email(self, obj):
        return  obj.i_auth_user.email

    def username(self, obj):
        return  obj.i_auth_user.username

    def is_active(self, obj):
        return  obj.i_auth_user.is_active


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_filter = ('i_auth_user__is_active','i_auth_user__email')
    list_display = ['email', 'username', 'is_active']

    def email(self, obj):
        return  obj.i_auth_user.email

    def username(self, obj):
        return  obj.i_auth_user.username

    def is_active(self, obj):
        return  obj.i_auth_user.is_active
