# Generated by Django 2.0.1 on 2018-01-14 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20180114_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshopenrollment',
            name='plan_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.WorkshopPlan'),
        ),
        migrations.AlterField(
            model_name='workshopenrollment',
            name='user_contact',
            field=models.CharField(max_length=20),
        ),
    ]
