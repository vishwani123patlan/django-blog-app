# Generated by Django 3.0.11 on 2020-12-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20201203_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above To Read Blog Post....', max_length=250),
        ),
    ]
