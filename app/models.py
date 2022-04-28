from django.conf import settings
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
