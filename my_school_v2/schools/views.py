from django.shortcuts import render
from .models import School
# Create your views here.

def index(request):
    school_details = School.objects.all()
    context = {'school_data': school_details}
    return render(request, 'schools/schools_list.html', context)



def indexxxx(request):
    school_details = {"name":"Nyeri High School", "code":"1001"}
    student_details = {"name":"Brigid", "code":"1001"}
    context = {'school_detail': school_details}

    return render(request,'schools/schools_list.html', context)

def detailss(request,school_id):
    return render(request,'schools/schools_details.html',{"name":"School","code":"1001"})