# Generated by Django 2.0.1 on 2018-01-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20180114_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshopenrollment',
            name='ref_code',
            field=models.CharField(default='no', max_length=20),
        ),
    ]