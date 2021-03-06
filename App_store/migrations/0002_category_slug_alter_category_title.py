# Generated by Django 4.0.3 on 2022-04-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
