# Generated by Django 2.2.4 on 2019-08-05 14:34

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190804_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
