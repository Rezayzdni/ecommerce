# Generated by Django 3.1.4 on 2020-12-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(default='-', max_length=11),
        ),
    ]
