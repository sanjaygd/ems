# Generated by Django 2.2.4 on 2019-08-16 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_auto_20190816_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='update_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
