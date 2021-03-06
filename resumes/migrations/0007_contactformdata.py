# Generated by Django 2.2.4 on 2019-08-20 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_worksprofile_link'),
        ('resumes', '0006_auto_20190820_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(blank=True, max_length=500, null=True)),
                ('message', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Client')),
            ],
        ),
    ]
