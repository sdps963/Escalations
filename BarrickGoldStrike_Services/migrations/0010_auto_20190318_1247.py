# Generated by Django 2.1.7 on 2019-03-18 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BarrickGoldStrike_Services', '0009_alerts_function_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alerts',
            old_name='Estimated_Downtime_ID',
            new_name='Estimated_Downtime',
        ),
    ]
