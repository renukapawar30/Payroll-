# Generated by Django 3.2.8 on 2024-06-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0002_basicpayofmonth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpayofmonth',
            name='empno',
            field=models.IntegerField(),
        ),
    ]