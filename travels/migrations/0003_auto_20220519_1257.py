# Generated by Django 2.0.13 on 2022-05-19 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0002_auto_20220512_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
