from django.db import models
from django.contrib.auth.models import AbstractBaseUser #that's allowing me to edit on the defult iser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """helps Django to work with our custom user model"""

    def create_user(self, email, name, password=None):
        """create a new user profile object"""
        if not email:
            raise ValueError("Users must have email address.")

        email = self.normalize_email(email)

        """that's for normalizing the email"""
        user = self.model(email=email, name=name)
        """here we  create new user object and assign the normalized email to mail and the name that taken from the paramters """
        user.set_password(password)
        """we use set_password function to hash password and add it to the user object"""
        user.save(using=self.db)
        """save and return the user """
        return user


    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self.db)
        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ represents a user profile inside our system """
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """used to get the users full name"""
        return self.name
        """the name is defined up"""

    def get_short_name(self):

        """used to get users short name"""
        return self.name

    def __str__(self):
        """django used this in the admin showing fields """
        return f"{self.email}"

class ProfileFeedItem(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text