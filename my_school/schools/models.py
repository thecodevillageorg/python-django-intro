from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    no_of_students = models.IntegerField()
    
    class Meta:
        db_table = 'tbl_schools'