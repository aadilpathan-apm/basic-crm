from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    customer_id: models.UUIDField(primary_key=True, auto_created=True, editable=False)
    company_name: models.CharField(max_length=150)
    created_date: models.DateField(null=False, default=datetime.today)
    creator_id: models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    changed_date: models.DateField(null=False, default=datetime.today)
    changer_id: models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    is_deleted: models.BooleanField(null=False, default=False)
    deleted_date: models.DateField(null=True, default=datetime.today)
    deleter_id: models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    why_deleted: models.TextField(max_length=500)