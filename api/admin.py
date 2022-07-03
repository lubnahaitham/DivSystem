from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.

from api.models import PersonalData

TokenAdmin.raw_id_fields = ['user']


# admin.site.register(PersonalData)


class PersonalDataAdmin(UserAdmin):
    model = PersonalData
    list_display = ('email', 'username', 'phone_number')

admin.site.register(PersonalData, PersonalDataAdmin)
