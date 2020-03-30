from django.contrib import admin
from .models import School

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'address','no_of_students')

admin.site.register(School)
