# Generated by Django 4.0.5 on 2022-08-07 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0006_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
