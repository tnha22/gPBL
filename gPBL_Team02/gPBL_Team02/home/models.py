# Create your models here.
from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=255)
    id_company = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'person'