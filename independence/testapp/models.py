from django.db import models


class User_Data(models.Model):
    name = models.CharField(max_length=100)
