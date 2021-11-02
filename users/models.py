from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField
    role = models.CharField(max_length=20)

    class Meta:
        db_table = "users"
