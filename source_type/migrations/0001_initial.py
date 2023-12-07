# Generated by Django 4.2.7 on 2023-12-07 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceType',
            fields=[
                ('source_type_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('source_title', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField()),
                ('changed_date', models.DateTimeField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_date', models.DateTimeField(null=True)),
                ('why_deleted', models.TextField(max_length=500, null=True)),
                ('changer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_type_changer', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_type_creator', to=settings.AUTH_USER_MODEL)),
                ('deleter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_type_deleter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]