# Generated by Django 2.0 on 2018-01-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_workshop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=8),
        ),
    ]