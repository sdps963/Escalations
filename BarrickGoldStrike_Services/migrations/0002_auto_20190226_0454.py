# Generated by Django 2.1.7 on 2019-02-26 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarrickGoldStrike_Services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertsdropdown_table',
            name='Created_Timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='alertsdropdown_table',
            name='Updated_Timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]