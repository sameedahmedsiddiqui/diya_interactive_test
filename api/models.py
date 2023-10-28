from django.db import models
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True

class Patient(models.Model):
    i_auth_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.i_auth_user.email


class Counsellor(models.Model):
    i_auth_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.i_auth_user

class Appointment(models.Model):

    i_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    i_counsellor = models.ForeignKey(Counsellor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s | %s" % (self.i_patient, self.i_counsellor)