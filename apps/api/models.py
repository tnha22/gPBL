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
    image = models.ImageField(null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


class Shift(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    name = models.CharField(verbose_name='name',max_length=255)
    start_time = models.TimeField(verbose_name='starttime')
    end_time = models.TimeField(verbose_name='endtime')

    def __str__(self) -> str:
        return "%s %s" % (self.starttime,self.endtime)
    class Meta: 
        db_table = 'shift'


class Schedule(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    name = models.CharField(verbose_name='name',max_length=255)
    date = models.DateField(verbose_name='date')
    shiftid = models.ForeignKey(Shift,on_delete=models.CASCADE)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'schedule'