# Generated by Django 5.0.6 on 2024-06-20 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('can_import_users', 'Can import users'), ('can_export_users', 'Can export users'))},
        ),
    ]