# Generated by Django 2.2.5 on 2019-11-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20191126_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='productID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]