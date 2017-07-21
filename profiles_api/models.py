from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Help django work with our custom user model."""
    def create_user(self, email, name, password=None):
        """Create a new user profile object."""
        if not email:
            raise ValueError("User must have email address.")
        # Normalize the email address by lowercasing the domain part of it.
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # Set user password by set_password function
        user.set_password(password)
        user.save(using=self._db) # Save to db

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details"""
        user = self.create_user(email, name, password)
        # assign two user
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

# Define model as class
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Respends a "user profile" inside our system
    """
    # unique : email cannot duplicate
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # Function get fullname
    def get_full_name(self):
        """Used to get a users full name"""
        return self.name

    def get_short_name(self):
        """Used to get a users short name"""
        return self.name

    def __str__(self):
        """Convert object to string"""
        return self.email

