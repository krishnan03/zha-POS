# Generated by Django 2.1b1 on 2018-08-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpage', '0004_auto_20180808_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='oldTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.TextField()),
            ],
        ),
    ]
