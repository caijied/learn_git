# Generated by Django 3.2.8 on 2022-10-08 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nav', '0007_auto_20221008_1334'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='car',
            unique_together={('name', 'unit_type')},
        ),
    ]
