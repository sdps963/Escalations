# Generated by Django 2.1.7 on 2019-04-18 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarrickGoldStrike_Services', '0018_alerts_owner_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerts',
            name='Escalated_On',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='alerts',
            name='Resolved_On',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
