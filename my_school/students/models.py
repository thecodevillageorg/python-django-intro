from django.db import models
from schools.models import School

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    parent_mobile = models.CharField(max_length=100, null=True)
    parent_name = models.CharField(max_length=100, null = True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_students'