# Generated by Django 2.2.4 on 2019-08-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quetions', models.ForeignKey(on_delete='CASCADE', to='poll.Question')),
            ],
        ),
    ]