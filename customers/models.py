from django.db import models
from django.contrib.auth.models import User
import uuid

class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, editable=False)
    company_name = models.CharField(null=False, max_length=150)
    email_address = models.EmailField(null=True)
    mobile_number = models.CharField(null=True, max_length=15)
    address_line_1: models.CharField(null=True, max_length=150)
    address_line_2: models.CharField(null=True, max_length=150)
    pincode: models.CharField(null=True, max_length=6)
    city: models.CharField(null=True, max_length=100)
    state: models.CharField(null=True, max_length=100)
    country: models.CharField(null=True, max_length=50)
    created_date = models.DateTimeField(null=False)
    creator = models.ForeignKey(User, null=False, related_name='customer_creator', on_delete=models.CASCADE)
    changed_date = models.DateTimeField(null=False)
    changer = models.ForeignKey(User, null=False, related_name='customer_changer', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(null=False, default=False)
    deleted_date = models.DateTimeField(null=True)
    deleter = models.ForeignKey(User, null=True, related_name='customer_deleter', on_delete=models.CASCADE)
    why_deleted = models.TextField(null=True, max_length=500)