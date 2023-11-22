from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=180)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'userauth'


User._meta.get_field('groups').remote_field.related_name = 'userauth_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'userauth_user_permissions'

class Email(models.Model):
    address = models.EmailField(unique=True)

    def __str__(self):
        return self.address