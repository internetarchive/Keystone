# Generated by Django 4.2.7 on 2024-07-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keystone', '0012_alter_account_max_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobfile',
            name='line_count',
            field=models.PositiveBigIntegerField(),
        ),
    ]
