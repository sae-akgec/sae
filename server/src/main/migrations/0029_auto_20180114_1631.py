# Generated by Django 2.0.1 on 2018-01-14 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20180114_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshopenrollment',
            name='user_local',
        ),
        migrations.AlterField(
            model_name='workshopenrollment',
            name='team_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='workshopenrollment',
            name='user_college',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workshopenrollment',
            name='user_contact',
            field=models.IntegerField(),
        ),
    ]
