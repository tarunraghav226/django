# Generated by Django 2.2.5 on 2019-11-26 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20191120_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.AddField(
            model_name='item',
            name='productID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
