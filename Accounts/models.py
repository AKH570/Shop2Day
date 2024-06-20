from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
        email=self.normalize_email(email),
        username=username,
        first_name=first_name,
        last_name=last_name,

    )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name,last_name,username,email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active= True
        user.is_staff = True
        user.is_superadmin=True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    SHOPE    = 1
    CUSTOMER= 2
    ROLE_CHOICE =(
        (SHOPE,'Shope'),
        (CUSTOMER,'Customer'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,unique=True)
    email   = models.EmailField(max_length=100,unique=True)
    phone_no = models.CharField(max_length=13,null=True,blank=True)
    role    = models.PositiveSmallIntegerField(choices=ROLE_CHOICE,blank=True,null=True)
    checkbox = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_login = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
    