# Generated by Django 5.0.6 on 2024-06-24 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
