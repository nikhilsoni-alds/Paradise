# Generated by Django 5.0.7 on 2024-08-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_alter_profile_designation_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='table_no',
            field=models.CharField(max_length=20),
        ),
    ]