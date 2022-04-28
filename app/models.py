from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

USER_STATUS = (
    ('Company', 0),
    ('Agency', 1),
)
COMP_STATUS = (
    ('Cool-Roof', 0),
    ('Road-Line', 1),
)


class User(AbstractBaseUser, models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=16)
    user_type = models.CharField(max_length=32, choices=USER_STATUS)
    email_auth = models.BooleanField(default=False)

    USERNAME_FIELD = 'id'

    def __str__(self):
       return str(self.user_id)

    class Meta:
        db_table = 'User'


class Agency(User, models.Model):
    area = models.CharField(max_length=32)

    class Meta:
        db_table = 'Agency'


class Company(User, models.Model):
    comp_category = models.CharField(max_length=32, choices=COMP_STATUS)
    comp_name = models.CharField(max_length=32)
    comp_homepage = models.CharField(max_length=64)

    class Meta:
        db_table = 'Company'
