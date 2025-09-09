from django.db import models

class StudentRecord(models.Model):
    student_id = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    year_level = models.IntegerField()
    date_registered = models.DateField()

    def __str__(self):
        return self.full_name