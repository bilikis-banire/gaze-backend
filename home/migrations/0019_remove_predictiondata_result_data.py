# Generated by Django 5.1.3 on 2024-11-28 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_predictiondata_result_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictiondata',
            name='result_data',
        ),
    ]
