# Generated by Django 2.1.7 on 2019-04-16 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarrickGoldStrike_Services', '0013_auto_20190415_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='Function_Area1_ID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customers',
            name='Function_Area2_ID',
            field=models.IntegerField(default=0),
        ),
    ]
