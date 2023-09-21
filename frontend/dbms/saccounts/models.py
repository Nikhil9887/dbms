from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields here
    cllg_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    pemail = models.EmailField()
    pno = models.IntegerField()

    # Additional custom fields (if needed)
    
