# Generated by Django 2.2.4 on 2019-08-05 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_sitesettings_data'),
        ('blogs', '0002_auto_20190805_1614'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='blogcategory',
            unique_together={('category', 'site')},
        ),
    ]
