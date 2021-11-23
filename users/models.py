from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone_number or not email:
            raise ValueError("The email or phone number must be set")
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number=None, email=None, password=None, **extra_fields):
        return self._create_user(phone_number, email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone_number = models.BigIntegerField(unique=True, blank=True)
    email = models.EmailField(unique=True)
    dob = models.DateField()

    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email", "phone_number"]
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)
