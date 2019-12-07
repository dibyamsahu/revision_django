from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("demo_app:detail", kwargs={"pk": self.pk})
    
    
class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name="students")

    def __str__(self):
        return self.name
    