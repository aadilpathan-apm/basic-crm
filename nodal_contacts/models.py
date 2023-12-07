from django.db import models
from django.contrib.auth.models import User
import uuid

from customers.models import Customer

class NodalContact(models.Model):
    nodal_contact_id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, editable=False)
    customer_id: models.ForeignKey(Customer, null=True, related_name='related_customer', on_delete=models.CASCADE)
    first_name: models.CharField(null=False, max_length=30)
    last_name: models.CharField(null=False, max_length=30)
    mobile_number: models.CharField(null=False, max_length=15)
    email_address: models.EmailField(null=True)
    is_primary_contact: models.BooleanField(null=False, default=False)
    created_date = models.DateTimeField(null=False)
    creator = models.ForeignKey(User, null=False, related_name='nodal_contact_creator', on_delete=models.CASCADE)
    changed_date = models.DateTimeField(null=False)
    changer = models.ForeignKey(User, null=False, related_name='nodal_contact_changer', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(null=False, default=False)
    deleted_date = models.DateTimeField(null=True)
    deleter = models.ForeignKey(User, null=True, related_name='nodal_contact_deleter', on_delete=models.CASCADE)
    why_deleted = models.TextField(null=True, max_length=500)