# Generated by Django 2.0 on 2018-01-09 11:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0020_auto_20180109_1716'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_profile',
            new_name='UserProfile',
        ),
    ]
