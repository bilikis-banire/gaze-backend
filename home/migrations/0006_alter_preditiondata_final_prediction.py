# Generated by Django 5.1.2 on 2024-11-02 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_preditiondata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preditiondata',
            name='final_prediction',
            field=models.CharField(),
        ),
    ]
