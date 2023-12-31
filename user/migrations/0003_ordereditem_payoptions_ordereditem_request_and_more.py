# Generated by Django 4.2.4 on 2023-10-31 12:52

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_ordereditem_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordereditem',
            name='payoptions',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='request',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='size',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='temp',
            field=models.CharField(default=datetime.datetime(2023, 10, 31, 12, 52, 10, 862049, tzinfo=datetime.timezone.utc), max_length=20),
            preserve_default=False,
        ),
    ]
