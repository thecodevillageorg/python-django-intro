from django.shortcuts import render

# Create your views here.

def index(request):
    studentDetails = {"name":'John',"regNo":"633676736"}
    context = {"student_detail": studentDetails}
    return render(request,'students/students_list.html', context)
