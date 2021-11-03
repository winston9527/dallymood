from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False)
    role = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        db_table = "users"
