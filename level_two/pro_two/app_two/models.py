from django.db import models

# Create your models here.

class UserDetail(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True,max_length=254)

    def __str__(self):
        return self.first_name
    