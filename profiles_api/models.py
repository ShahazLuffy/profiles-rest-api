from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ manager for user profile"""

    def create_user(self, email, name, password=None):
        """ create a new user profile """
        if not email:
            raise ValueError('user must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ DataBase model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)  # 2 users can't use same email
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    # we need a model manager for our custom user model to know how to create users and control users

    # we need some fields for django admin and django admin authentication
    USERNAME_FIELD = 'email'  # we are overriding default USERNAME_FIELD  which normally call username
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ retrieve the full name of the user """
        return self.name

    def get_short_name(self):
        """ retrieve short name of user"""
        return self.name

    def __str__(self):
        """ return the string representation of our user """
        return self.email
