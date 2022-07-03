from django.test import TestCase

# Create your tests here.
from django.contrib import auth
from django.contrib.auth.models import User

from api.models import PersonalData

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = PersonalData.objects.create_user(phone_number='11256566', username='test', password='pass')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(phone_number='11256566', password='pass')