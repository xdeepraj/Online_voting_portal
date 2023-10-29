from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):

    username        = None
    email           = models.EmailField(('email address'), unique=True)
    id_card_no      = models.CharField(max_length=15, unique=True, blank=False)
    first_name      = models.CharField(max_length=150, blank=False)
    last_name       = models.CharField(max_length=150, blank=False)
    mobile_no       = models.CharField(max_length=10, blank=True)
    address         = models.CharField(max_length=255)
    profile_image   = models.ImageField(upload_to="user_images/", null=True, blank=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["id_card_no"]

    def __str__(self):
        return self.first_name + self.last_name





    





