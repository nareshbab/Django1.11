from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
# Create your models here.
import json

class Permission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(unique=True)
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(unique=True)
    display_name = models.CharField(max_length=255)
    permissions = models.ManyToManyField(Permission, auto_created=True)

    def __str__(self):
        return self.display_name


class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    display_name = models.CharField(max_length=255, unique=True)
    roles = models.ManyToManyField(Role, auto_created=True)

    def __str__(self):
        return self.display_name


class UserManager(BaseUserManager):
    def create_user(self, username, email, user_id, password=None, is_active =True, is_staff=False, is_admin=False, permissions=None):
        if not email:
            raise ValueError("Users must have an email")
        if not password:
            raise ValueError("Users must have a password")
        if not username:
            raise ValueError("Users must have a unique username")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.username = username
        user_obj.permissions = permissions
        user_obj.user_id = user_id
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, email, user_id, password=None, permissions=None):
        user = self.create_user(
            email,
            username,
            user_id,
            permissions=permissions,
            password=password,
            is_staff=True
        )
        return user

    def create_adminuser(self, username, email, user_id, password=None, permissions=None):
        user = self.create_user(
            email,
            username,
            user_id,
            permissions=permissions,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user

    def create_superuser(self, username, email, user_id, password=None, permissions=None):
        user = self.create_user(
            email,
            username,
            user_id,
            permissions=permissions,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, max_length=255)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)
    permissions = models.ManyToManyField(Group, auto_created=True)
    # confirm = models.DateTimeField(default=False)

    USERNAME_FIELD = 'email'  #username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ['username', 'user_id']

    object = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def get_username(self):
        return self.username

    def get_userid(self):
        return self.user_id

    def get_permissions(self):
        return self.permissions

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True



class Profile(models.Model):
    user = models.OneToOneField(User)


class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.TimeField(auto_now=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email


