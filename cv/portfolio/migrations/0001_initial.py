# Generated by Django 2.1.7 on 2019-07-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('mot_name', models.CharField(max_length=30)),
                ('From', models.CharField(max_length=30)),
                ('current', models.CharField(max_length=30)),
                ('school', models.CharField(max_length=30)),
                ('university', models.CharField(max_length=30)),
                ('x', models.CharField(max_length=30)),
                ('xii', models.CharField(max_length=30)),
                ('hobbies', models.CharField(max_length=30)),
                ('skills', models.TextField()),
                ('desc', models.TextField()),
                ('dp', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
