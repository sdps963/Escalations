# Generated by Django 2.1.7 on 2019-03-11 21:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarrickGoldStrike_Services', '0006_auto_20190311_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estimated_Downtime_Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estimated_Dropdown', models.CharField(max_length=200)),
                ('Created_Timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('Updated_Timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='alerts',
            old_name='status',
            new_name='Status',
        ),
        migrations.AlterField(
            model_name='alerts',
            name='Date_of_Occurance',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='alerts',
            name='Location_Coordinates',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='customers',
            name='Created_Timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='Updated_Timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='dropdown_table_associations',
            name='Created_Timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='dropdown_table_associations',
            name='Updated_Timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='severity_level',
            name='Created_Timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='severity_level',
            name='Updated_Timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
