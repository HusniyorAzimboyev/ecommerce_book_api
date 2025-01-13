from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model where phone_number is the unique identifier.
    """

    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Create and return a regular user with the given phone number and password.
        """
        if not phone_number:
            raise ValueError("The phone number must be set")

        # Normalize the phone number (custom normalization logic can be added here)
        phone_number = phone_number.strip()
        extra_fields.setdefault("is_active", True)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """
        Create and return a superuser with the given phone number and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model where phone_number is the unique identifier for authentication
    instead of username.
    """
    phone_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    # Permissions fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Timestamps
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    # Custom manager
    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"  # Unique identifier for authentication
    REQUIRED_FIELDS = []  # Fields required for creating superusers (apart from phone_number)

    def __str__(self):
        return self.phone_number
