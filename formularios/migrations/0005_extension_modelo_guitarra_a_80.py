# Generated by Django 3.1.6 on 2021-02-17 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0004_auto_20210217_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitarra',
            name='modelo',
            field=models.CharField(max_length=80),
        ),
    ]
