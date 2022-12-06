# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # Delete not use field
    first_name = None
    last_name = None
    last_login = None
    is_staff = None
    is_superuser = None

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    id_company = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=True)
    is_unknown = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


class Shift(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField(default=True)
    end_time = models.TimeField(default=True)
    status = models.BooleanField(default=True)
    date = models.DateField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)

    def __str__(self) -> str:
        return "%s %s" % (self.start_time,self.end_time)
    class Meta: 
        db_table = 'shift'
    
class Camera(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)

    class Meta:
        db_table = 'camera'

class Face(models.Model):
    name = models.CharField(max_length=50)
    feature = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'face'


class Log(models.Model):
    time_in = models.TimeField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    camera = models.ForeignKey(Face, on_delete=models.PROTECT)

    class Meta:
        db_table = 'log'