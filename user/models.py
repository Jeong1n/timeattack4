from django.db import models
# Create your models here.

class user(models.Model):
    class Meta:
        db_table = "my_user"

    email = models.CharField(max_length=256, default='')
    password = models.CharField(max_length=256, default='')