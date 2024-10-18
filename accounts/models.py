from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models



class User(AbstractUser):
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True,
                                    validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
