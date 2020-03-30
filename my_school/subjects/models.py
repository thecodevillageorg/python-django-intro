from django.db import models

# Create your models here.
from django.db import models
from students.models import Student
from schools.models import School
# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=1)
    
    class Meta:
        db_table = 'tbl_subjects'