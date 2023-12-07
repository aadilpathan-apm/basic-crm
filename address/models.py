import uuid

from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, editable=False)
    address_line_1 = models.CharField(null=True, max_length=150)
    address_line_2 = models.CharField(null=True, max_length=150)
    pincode = models.CharField(null=True, max_length=6)
    city = models.CharField(null=True, max_length=100)
    state = models.CharField(null=True, max_length=100)
    country = models.CharField(null=True, max_length=50)
    created_date = models.DateTimeField(null=False)
    creator = models.ForeignKey(User, null=False, related_name='address_creator', on_delete=models.CASCADE)
    changed_date = models.DateTimeField(null=False)
    changer = models.ForeignKey(User, null=False, related_name='address_changer', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(null=False, default=False)
    deleted_date = models.DateTimeField(null=True)
    deleter = models.ForeignKey(User, null=True, related_name='address_deleter', on_delete=models.CASCADE)
    why_deleted = models.TextField(null=True, max_length=500)