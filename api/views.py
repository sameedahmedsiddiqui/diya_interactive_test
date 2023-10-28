import datetime
from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from api.models import Patient, Counsellor, Appointment
from api.utils import get_random_string


@api_view(['GET'])
def apis_info(request):
    api_urls = {
        'all active patients' : 'get_all_active_patients/',
        'all active counsellors' : 'get_all_active_counsellors/',
        'all active appointments' : 'get_all_active_appointments/',
    }
    return Response(api_urls)


@api_view(['GET'])
def get_all_active_patients(request):
    response = {'status': False, 'errors':[]}
    data = []
    try:
        all_patients = Patient.objects.filter(i_auth_user__is_active=True)
        for patient in all_patients:
            row = dict()
            row['username'] = patient.i_auth_user.username
            row['email'] = patient.i_auth_user.email
            row['user_role'] = 'Patient'
            row['is_active'] = patient.i_auth_user.is_active
            data.append(row)
        response['status'] = True
        response['data'] = data
    except Exception as e:
        response['status'] = False
        response['errors'].append(repr(e))
    return Response(response)


@api_view(['GET'])
def get_all_active_counsellors(request):
    response = {'status': False, 'errors': []}
    data = []
    try:
        all_counsellors = Counsellor.objects.filter(i_auth_user__is_active=True)
        for counsellor in all_counsellors:
            row = dict()
            row['username'] = counsellor.i_auth_user.username
            row['email'] = counsellor.i_auth_user.email
            row['user_role'] = 'Counsellor'
            row['is_active'] = counsellor.i_auth_user.is_active
            data.append(row)
        response['status'] = True
        response['data'] = data
    except Exception as e:
        response['status'] = False
        response['errors'].append(repr(e))
    return Response(response)


@api_view(['GET'])
def get_all_active_appointments(request):
    response = {'status': False, 'errors': []}
    data = []
    try:
        appointments = Appointment.objects.filter(is_active=True)
        for appointment in appointments:
            row = dict()
            row['patient_email'] = appointment.i_patient.i_auth_user.email
            row['counsellor_email'] = appointment.i_counsellor.i_auth_user.email
            row['appointment_date'] = appointment.appointment_date
            row['is_active'] = appointment.is_active
            data.append(row)
        response['status'] = True
        response['data'] = data
    except Exception as e:
        response['status'] = False
        response['errors'].append(repr(e))
    return Response(response)


@api_view(['POST'])
def create_patient(request):
    response  = {'status': False, 'errors':[]}
    try:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        patient_name = "%s.%s_%s" %(first_name, last_name, get_random_string())
        patient_email = request.POST.get('patient_email')
        patient_password = request.POST.get('patient_password')
        if len(patient_password) < 8:
            response['status'] = False
            response['errors'].append("Please Enter a Password of atleast 8 digit")
        else:
            user = User.objects.create_user(username=patient_name, email=patient_email, password=patient_password)
            patient = Patient.objects.create(i_auth_user=user)
            response['status'] = True
            response['message'] = "Patient Created With Email %s and ID %s" % (patient_email, str(patient.pk))
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)



@api_view(['POST'])
def create_counsellor(request):
    response  = {'status': False, 'errors':[]}
    try:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        counsellor_name = "%s.%s_%s" %(first_name, last_name, get_random_string())
        counsellor_email = request.POST.get('counsellor_email')
        counsellor_password = request.POST.get('counsellor_password')
        if len(counsellor_password) < 8:
            response['status'] = False
            response['errors'].append("Please Enter a Password of atleast 8 digit")
        else:
            user = User.objects.create_user(username=counsellor_name, email=counsellor_email, password=counsellor_password)
            patient = Counsellor.objects.create(i_auth_user=user)
            response['status'] = True
            response['message'] = "Counsellor Created With Email %s and ID %s" % (counsellor_email, str(patient.pk))
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)


@api_view(['POST'])
def update_counsellor(request):
    response = {'status': False, 'errors':[]}
    try:
        counsellor_id = request.POST.get('counsellor_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        counsellor_name = "%s.%s_%s" %(first_name, last_name, get_random_string())
        counsellor_email = request.POST.get('counsellor_email')
        counsellor_password = request.POST.get('counsellor_password')
        counsellor_obj = Counsellor.objects.get(pk=counsellor_id)
        counsellor_obj.i_auth_user.username = counsellor_name
        counsellor_obj.i_auth_user.email = counsellor_email
        counsellor_obj.i_auth_user.password = counsellor_password
        counsellor_obj.i_auth_user.save()
        counsellor_obj.save()
        response['status'] = True
        response['message'] = "Counsellor Updated With Email %s and ID %s" % (counsellor_email, str(counsellor_obj.pk))
    except Counsellor.DoesNotExist:
        response['errors'].append('Counsellor with counsellor ID %s not exists' % (str(counsellor_id)))
        response['status'] = False
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)


@api_view(['POST'])
def update_patient(request):
    response = {'status': False, 'errors':[]}
    try:
        patient_id = request.POST.get('patient_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        patient_name = "%s.%s_%s" % (first_name, last_name, get_random_string())
        patient_email = request.POST.get('patient_email')
        patient_password = request.POST.get('patient_password')
        patient_obj = Patient.objects.get(pk=patient_id)
        patient_obj.i_auth_user.username = patient_name
        patient_obj.i_auth_user.email = patient_email
        patient_obj.i_auth_user.password = patient_password
        patient_obj.i_auth_user.save()
        patient_obj.save()
        response['status'] = True
        response['message'] = "Patient Updated With Email %s and ID %s" % (patient_email, str(patient_obj.pk))
    except Patient.DoesNotExist:
        response['errors'].append('Patient with Patient ID %s not exists' % (str(patient_id)))
        response['status'] = False
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)


@api_view(['GET'])
def get_specific_patient_record(request):
    response = {'status': True, 'errors':[]}
    data_dict = {}
    try:
        patient_email = request.GET.get('patient_email')
        patient_obj = Patient.objects.get(i_auth_user__email=patient_email)
        data_dict['username'] = patient_obj.i_auth_user.username
        data_dict['email'] = patient_obj.i_auth_user.email
        data_dict['user_role'] = 'patient'
        data_dict['is_active'] = patient_obj.i_auth_user.is_active
        response['data'] = data_dict
    except Patient.DoesNotExist as e:
        response['errors'].append('Patient with Patient Email %s not exists' % (patient_email))
        response['status'] = False
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)


@api_view(['GET'])
def get_specific_counsellor_record(request):
    response = {'status': True, 'errors':[]}
    data_dict = {}
    try:
        counsellor_email = request.GET.get('counsellor_email')
        counsellor_obj = Counsellor.objects.get(i_auth_user__email=counsellor_email)
        data_dict['username'] = counsellor_obj.i_auth_user.username
        data_dict['email'] = counsellor_obj.i_auth_user.email
        data_dict['user_role'] = 'counsellor'
        data_dict['is_active'] = counsellor_obj.i_auth_user.is_active
        response['data'] = data_dict
    except Counsellor.DoesNotExist as e:
        response['errors'].append('Counsellor with Counsellor Email %s not exists' % (counsellor_email))
        response['status'] = False
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)


@api_view(['POST'])
def delete_counsellor(request):
    response = {'status': True, 'errors':[]}
    try:
        counsellor_email = request.POST.get('counsellor_email')
        counsellor_obj = Counsellor.objects.get(i_auth_user__email=counsellor_email)
        counsellor_obj.i_auth_user.is_active = False
        counsellor_obj.i_auth_user.save()
        counsellor_obj.save()
        response['message'] = "Counsellor with Email %s Deleted" % (counsellor_email)
        response['status'] = True
    except Counsellor.DoesNotExist as e:
        response['errors'].append('Counsellor with Counsellor Email %s not exists' % (counsellor_email))
        response['status'] = False
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)


@api_view(['POST'])
def delete_patient(request):
    response = {'status': True, 'errors':[]}
    try:
        patient_email = request.POST.get('patient_email')
        patient_obj = Patient.objects.get(i_auth_user__email=patient_email)
        patient_obj.i_auth_user.is_active = False
        patient_obj.i_auth_user.save()
        patient_obj.save()
        response['message'] = "Pateint with Email %s Deleted" % (patient_email)
        response['status'] = True
    except Patient.DoesNotExist as e:
        response['errors'].append('Patient with Patient Email %s not exists' % (patient_email))
        response['status'] = False
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)


@api_view(['POST'])
def delete_appointment(request):
    response = {'status': True, 'errors':[]}
    try:
        appointment_id = request.POST.get('appointment_id')
        appointment_obj = Appointment.objects.get(pk=appointment_id)
        appointment_obj.is_active = False
        appointment_obj.save()
        response['message'] = "Appointment with Appointment ID %s Deleted" % (appointment_id)
        response['status'] = True
    except Appointment.DoesNotExist as e:
        response['errors'].append('Appointment with Appointment ID %s not exists' % (appointment_id))
        response['status'] = False
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)


@api_view(['GET'])
def get_patient_all_appointments(request):
    response = {'status': False, 'errors':[]}
    data = []
    try:
        patient_email = request.GET.get('patient_email')
        all_appointments = Appointment.objects.filter(i_patient__i_auth_user__email= patient_email)
        for appointment in all_appointments:
            row = dict()
            row['patient_email'] = appointment.i_patient.i_auth_user.email
            row['counsellor_email'] = appointment.i_counsellor.i_auth_user.email
            row['appointment_date'] = appointment.appointment_date
            row['is_active'] = appointment.is_active
            data.append(row)
        response['status'] = True
        response['data'] = data
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)


@api_view(['GET'])
def get_counsellor_all_appointments(request):
    response = {'status': False, 'errors':[]}
    data = []
    try:
        counsellor_email = request.GET.get('counsellor_email')
        all_appointments = Appointment.objects.filter(i_counsellor__i_auth_user__email=counsellor_email)
        for appointment in all_appointments:
            row = dict()
            row['patient_email'] = appointment.i_patient.i_auth_user.email
            row['counsellor_email'] = appointment.i_counsellor.i_auth_user.email
            row['appointment_date'] = appointment.appointment_date
            row['is_active'] = appointment.is_active
            data.append(row)
        response['status'] = True
        response['data'] = data
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)


@api_view(['GET'])
def get_all_appointments_specific_date_range(request):
    response = {'status': False, 'errors':[]}
    data = []
    try:

        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        all_appointments = Appointment.objects.filter(appointment_date__lte=end_date, appointment_date__gte=start_date).order_by('-appointment_date')
        for appointment in all_appointments:
            row = dict()
            row['patient_email'] = appointment.i_patient.i_auth_user.email
            row['counsellor_email'] = appointment.i_counsellor.i_auth_user.email
            row['appointment_date'] = appointment.appointment_date
            row['is_active'] = appointment.is_active
            data.append(row)
        response['status'] = True
        response['data'] = data
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)


@api_view(['POST'])
def create_appointment(request):
    response = {'status': True, 'errors':[]}
    try:
        i_patient = request.POST.get('i_patient_id')
        i_counsellor = request.POST.get('i_counsellor_id')
        appointment_date = request.POST.get('appointment_date')
        final_date = datetime.datetime.strptime(appointment_date, '%d/%m/%y %H:%M:%S')
        patient_obj = Patient.objects.get(pk=i_patient)
        patient_all_appointment = Appointment.objects.filter(i_patient=patient_obj)
        dates = list(data.appointment_date.strftime('%d/%m/%y %H:%M:%S') for data in patient_all_appointment)
        if final_date.strftime('%d/%m/%y %H:%M:%S') in dates:
            response['status'] = False
            response['errors'].append('Unable To create appointment because patient have same appointment in this slot')
            return Response(response)
        counsellor_obj = Counsellor.objects.get(pk=i_counsellor)
        counsellor_all_appointment = Appointment.objects.filter(i_counsellor=counsellor_obj)
        dates = list(data.appointment_date.strftime('%d/%m/%y %H:%M:%S') for data in counsellor_all_appointment)
        if final_date.strftime('%d/%m/%y %H:%M:%S') in dates:
            response['status'] = False
            response['errors'].append('Unable To create appointment because Counsellor have same appointment in this slot')
            return Response(response)
        if patient_obj.i_auth_user.is_active:
            if counsellor_obj.i_auth_user.is_active:
                Appointment.objects.create(i_patient=patient_obj,i_counsellor=counsellor_obj,appointment_date=final_date)
                response['status'] = True
                response['message'] = 'Your appointment has been created'
            else:
                response['status'] = False
                response['errors'].append('Unable to Create Appointment Because Your Counsellor is Deactivated')
        else:
            response['status'] = False
            response['errors'].append('Unable to Create Appointment Because Your Patient is Deactivated')
    except Patient.DoesNotExist as e:
        response['errors'].append('Patient with Pateint ID %s not exists' % (i_patient))
        response['status'] = False
    except Counsellor.DoesNotExist as e:
        response['errors'].append('Counsellor with Counsellor ID %s not exists' % (i_counsellor))
        response['status'] = False
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)


@api_view(['POST'])
def update_appointment(request):
    response = {'status': True, 'errors':[]}
    try:
        appointment_id = request.POST.get('appointment_id')
        i_patient = request.POST.get('i_patient_id')
        i_counsellor = request.POST.get('i_counsellor_id')
        appointment_date = request.POST.get('appointment_date')
        final_date = datetime.datetime.strptime(appointment_date, '%d/%m/%y %H:%M:%S')
        appointment_obj = Appointment.objects.get(pk=appointment_id)
        patient_obj = Patient.objects.get(pk=i_patient)
        counsellor_obj = Counsellor.objects.get(pk=i_counsellor)
        if patient_obj.i_auth_user.is_active:
            if counsellor_obj.i_auth_user.is_active:
                appointment_obj.i_patient = patient_obj
                appointment_obj.i_counsellor = counsellor_obj
                appointment_obj.appointment_date = final_date
                appointment_obj.save()
                response['status'] = True
                response['message'] = 'Your appointment has been created'
            else:
                response['status'] = False
                response['errors'].append('Unable to Update Appointment Because Your Counsellor is Deactivated')
        else:
            response['status'] = False
            response['errors'].append('Unable to Update Appointment Because Your Patient is Deactivated')

    except Appointment.DoesNotExist as e:
        response['errors'].append('Appointment with Appointment ID %s not exists' % (appointment_id))
        response['status'] = False
    except Patient.DoesNotExist as e:
        response['errors'].append('Patient with Pateint ID %s not exists' % (i_patient))
        response['status'] = False
    except Counsellor.DoesNotExist as e:
        response['errors'].append('Counsellor with Counsellor ID %s not exists' % (i_counsellor))
        response['status'] = False
    except Exception as e:
        response['errors'].append(repr(e))
        response['status'] = False
    return Response(response)

