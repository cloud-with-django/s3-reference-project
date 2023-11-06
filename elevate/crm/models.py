from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):

    profile_pic = models.ImageField(null=True, blank=True)

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)



