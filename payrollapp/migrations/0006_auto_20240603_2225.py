# Generated by Django 3.2.8 on 2024-06-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0005_auto_20240603_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpayofmonth',
            name='empno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='incometax',
            name='empno',
            field=models.IntegerField(),
        ),
    ]
