from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    account_id = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

class Picture(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    picture_name = models.CharField(max_length=200)

    def __str__(self):
        return self.picture_name
