from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=65)
    lastName = models.CharField(max_length=65)
    email = models.CharField(max_length=80)
    interests = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName
    
