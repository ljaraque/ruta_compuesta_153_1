# Generated by Django 3.1.6 on 2021-02-17 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0003_auto_20210216_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitarra',
            name='marca',
            field=models.CharField(max_length=80),
        ),
    ]