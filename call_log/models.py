import uuid
from django.db import models
from django.contrib.auth.models import User

from lead.models import Lead
from contact_person.models import ContactPerson

class CallLog(models.Model):
    CALL_TYPES = [
        ("I", "Incoming"),
        ("O", "Outgoing"),
        ("M", "Missed")
    ]
    call_log_id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, editable=False)
    caller = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, null=False, on_delete=models.CASCADE)
    contact_person = models.ForeignKey(ContactPerson, null=False, on_delete=models.CASCADE)
    call_type = models.CharField(null=False, max_length=1, choices=CALL_TYPES, default=None)
    calling_time = models.DateTimeField(null=True, default=None)
    call_duration = models.TimeField(null=True, default=None)
    purpose_of_the_call = models.TextField(null=True, max_length=1000, default='')
    outcome_of_the_call = models.TextField(null=True, max_length=1000, default='')
    is_call_recording_available = models.BooleanField(null=False, default=False)
    call_recording_urls = models.JSONField(null=True, default=dict)
    created_date = models.DateTimeField(null=False)
    creator = models.ForeignKey(User, null=False, related_name='call_log_creator', on_delete=models.CASCADE)
    changed_date = models.DateTimeField(null=False)
    changer = models.ForeignKey(User, null=False, related_name='call_log_changer', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(null=False, default=False)
    deleted_date = models.DateTimeField(null=True)
    deleter = models.ForeignKey(User, null=True, related_name='call_log_deleter', on_delete=models.CASCADE)
    why_deleted = models.TextField(null=True, max_length=500)

    def __str__(self):        
        return f"{self.call_type} call with {self.contact_person.person_name} from {self.lead} by {self.caller}"