# Generated by Django 2.2.4 on 2019-08-18 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0008_auto_20190818_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='update_at',
            field=models.DateField(auto_now=True),
        ),
    ]