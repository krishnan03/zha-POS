# Generated by Django 2.1b1 on 2018-07-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=250)),
                ('productDesc', models.CharField(max_length=250)),
                ('productWt', models.CharField(max_length=10)),
                ('productPrice', models.CharField(max_length=10)),
            ],
        ),
    ]
