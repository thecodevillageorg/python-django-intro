from django.shortcuts import render
from .models import Subject

# Create your views here.
def index(request):
    subjects_list = Subject.objects.all() ## fetch data from database
    context = {'subject_data':subjects_list}
    return render(request,'subjects/subjects_list.html', context)

def detail(request):
    return render(request,'subjects/subject_detail.html',{})