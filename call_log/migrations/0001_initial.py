# Generated by Django 4.2.7 on 2023-12-07 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lead', '0001_initial'),
        ('contact_person', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CallLog',
            fields=[
                ('call_log_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('call_type', models.CharField(choices=[('I', 'Incoming'), ('O', 'Outgoing'), ('M', 'Missed')], default=None, max_length=1)),
                ('calling_time', models.DateTimeField(default=None, null=True)),
                ('call_duration', models.TimeField(default=None, null=True)),
                ('purpose_of_the_call', models.TextField(default='', max_length=1000, null=True)),
                ('outcome_of_the_call', models.TextField(default='', max_length=1000, null=True)),
                ('is_call_recording_available', models.BooleanField(default=False)),
                ('call_recording_urls', models.JSONField(default=dict, null=True)),
                ('created_date', models.DateTimeField()),
                ('changed_date', models.DateTimeField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_date', models.DateTimeField(null=True)),
                ('why_deleted', models.TextField(max_length=500, null=True)),
                ('caller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('changer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='call_log_changer', to=settings.AUTH_USER_MODEL)),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact_person.contactperson')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='call_log_creator', to=settings.AUTH_USER_MODEL)),
                ('deleter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='call_log_deleter', to=settings.AUTH_USER_MODEL)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lead.lead')),
            ],
        ),
    ]
