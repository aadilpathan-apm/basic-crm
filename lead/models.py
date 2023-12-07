import uuid
from django.db import models
from django.contrib.auth.models import User

from address.models import Address
from source_type.models import SourceType
from lead_type.models import LeadType

class Lead(models.Model):
    lead_id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, editable=False)
    company_name = models.CharField(null=False, max_length=150)
    email_address = models.EmailField(null=True)
    mobile_number = models.CharField(null=True, max_length=15)
    source_type = models.ForeignKey(SourceType, null=True, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    lead_type = models.ForeignKey(LeadType, null=False, on_delete=models.CASCADE)
    lelead_type_changed_date = models.DateTimeField(null=False)
    created_date = models.DateTimeField(null=False)
    creator = models.ForeignKey(User, null=False, related_name='lead_creator', on_delete=models.CASCADE)
    changed_date = models.DateTimeField(null=False)
    changer = models.ForeignKey(User, null=False, related_name='lead_changer', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(null=False, default=False)
    deleted_date = models.DateTimeField(null=True)
    deleter = models.ForeignKey(User, null=True, related_name='lead_deleter', on_delete=models.CASCADE)
    why_deleted = models.TextField(null=True, max_length=500)