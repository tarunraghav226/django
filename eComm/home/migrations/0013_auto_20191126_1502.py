# Generated by Django 2.2.5 on 2019-11-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20191126_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='productID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
