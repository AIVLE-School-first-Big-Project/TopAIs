from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

USER_STATUS = (
    ('Company', 0),
    ('Agency', 1),
)
COMP_STATUS = (
    ('Cool-Roof', 0),
    ('Road-Line', 1),
)


class UserManager(BaseUserManager):
    def _create_user(self, user_id, password, **extra_fields):
        if not user_id:
            raise ValueError('The given user_id must be set')
        user = self.model(
            user_id=user_id, **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_id = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=16)
    user_type = models.CharField(max_length=32, choices=USER_STATUS)
    email_auth = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'

    class Meta:
        db_table = 'User'


class Agency(User, models.Model):
    uid = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    area = models.CharField(max_length=32)

    class Meta:
        db_table = 'Agency'


class Company(User, models.Model):
    uid = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    comp_category = models.CharField(max_length=32, choices=COMP_STATUS)
    comp_name = models.CharField(max_length=32)
    comp_homepage = models.CharField(max_length=64)

    class Meta:
        db_table = 'Company'
