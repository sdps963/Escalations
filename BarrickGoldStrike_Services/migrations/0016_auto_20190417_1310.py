# Generated by Django 2.1.7 on 2019-04-17 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarrickGoldStrike_Services', '0015_auto_20190415_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerts',
            name='Escalation_Description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='alerts',
            name='Resolution_Description',
            field=models.CharField(default='', max_length=500),
        ),
    ]
