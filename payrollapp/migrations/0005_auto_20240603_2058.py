# Generated by Django 3.2.8 on 2024-06-03 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0004_incometax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpayofmonth',
            name='empno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payrollapp.empattendence'),
        ),
        migrations.AlterField(
            model_name='incometax',
            name='empno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payrollapp.empattendence'),
        ),
    ]