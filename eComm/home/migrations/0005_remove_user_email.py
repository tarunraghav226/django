# Generated by Django 2.2.5 on 2019-11-19 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
