# Generated by Django 2.0 on 2018-01-05 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180105_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('tech', models.CharField(max_length=200, unique=True)),
                ('details', models.TextField()),
                ('img', models.CharField(default='https://', max_length=200)),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Workshop')),
            ],
        ),
    ]
