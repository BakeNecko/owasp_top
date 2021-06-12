from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.username} - {self.password}'
