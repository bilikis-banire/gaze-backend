# Generated by Django 5.1.3 on 2024-11-27 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_predictiondata_result_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictiondata',
            name='result_data',
            field=models.CharField(default='Data not available', max_length=500),
        ),
    ]
