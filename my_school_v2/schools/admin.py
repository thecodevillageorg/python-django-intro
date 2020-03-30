from django.contrib import admin
from .models import School
# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name','code','address','no_of_students')

admin.site.register(School,SchoolAdmin)
