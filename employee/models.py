from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class Employee(AbstractBaseUser):
    
    id  = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255,  blank=True) 
    password = models.CharField(max_length=255 )
    email = models.CharField(max_length=255, unique=True, blank=True) 
    remark = models.CharField(max_length=255,  blank=True )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    last_login = None

    USERNAME_FIELD = 'email'

    def __str__(self) :
        return str(self.id)

    class Meta:
        db_table = "employee"
