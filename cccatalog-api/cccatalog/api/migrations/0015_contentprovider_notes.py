# Generated by Django 2.0.8 on 2019-01-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20190122_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentprovider',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
