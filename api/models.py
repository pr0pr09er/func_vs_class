from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=255)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gender']


choices = [
    ('toys', 'игрушки'),
    ('items', 'вещи'),
]


class Product(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=choices)


class Cart(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    price = models.IntegerField()
