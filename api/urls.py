from django.urls import path

from . import views

urlpatterns = [
    path('', views.apis_info, name='api_view'),
    path('get_all_active_patients/', views.get_all_active_patients, name='get_all_active_patients'),
    path('get_all_active_counsellors/', views.get_all_active_counsellors, name='get_all_active_counsellors'),
    path('get_all_active_appointments/', views.get_all_active_appointments, name='get_all_active_appointments'),
    path('create_patient/', views.create_patient, name='create_patient'),
    path('create_counsellor/', views.create_counsellor, name='create_counsellor'),
    path('update_counsellor/', views.update_counsellor, name='update_counsellor'),
    path('update_patient/', views.update_patient, name='update_patient'),
    path('get_specific_patient_record/', views.get_specific_patient_record, name='get_specific_patient_record'),
    path('get_specific_counsellor_record/', views.get_specific_counsellor_record, name='get_specific_counsellor_record'),
    path('delete_counsellor/', views.delete_counsellor, name='delete_counsellor'),
    path('delete_patient/', views.delete_patient, name='delete_patient'),
    path('delete_appointment/', views.delete_appointment, name='delete_appointment'),
    path('get_all_active_counsellors/', views.get_all_active_counsellors, name='get_all_active_counsellors'),
    path('get_patient_all_appointments/', views.get_patient_all_appointments, name='get_patient_all_appointments'),
    path('get_counsellor_all_appointments/', views.get_counsellor_all_appointments, name='get_counsellor_all_appointments'),
    path('get_all_appointments_specific_date_range/', views.get_all_appointments_specific_date_range, name='get_all_appointments_specific_date_range'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('update_appointment/', views.update_appointment, name='update_appointment'),
]
