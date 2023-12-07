from django.db import models

# Create your models here.


class File(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    size = models.IntegerField()
    owner = models.IntegerField()
    is_folder = models.BooleanField()
    parent = models.IntegerField()
    shared = models.BooleanField()
    shared_with = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class NUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)