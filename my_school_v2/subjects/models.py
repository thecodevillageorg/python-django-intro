from django.db import models

# Create your models here.
from django.db import models
from students.models import Student

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tbl_subjects'