import uuid
from django.db import models
from django.contrib.auth.models import User

class SourceType(models.Model):
    source_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, editable=False)
    source_title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    is_active = models.BooleanField(null=False, default=True)
    created_date = models.DateTimeField(null=False)
    creator = models.ForeignKey(User, null=False, related_name='source_type_creator', on_delete=models.CASCADE)
    changed_date = models.DateTimeField(null=False)
    changer = models.ForeignKey(User, null=False, related_name='source_type_changer', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(null=False, default=False)
    deleted_date = models.DateTimeField(null=True)
    deleter = models.ForeignKey(User, null=True, related_name='source_type_deleter', on_delete=models.CASCADE)
    why_deleted = models.TextField(null=True, max_length=500)

    def __str__(self):
        return self.source_title