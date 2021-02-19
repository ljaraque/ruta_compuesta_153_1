# Generated by Django 3.1.6 on 2021-02-18 21:56

import django.core.validators
from django.db import migrations, models
import formularios.models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0005_extension_modelo_guitarra_a_80'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuitarraCBV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(3, 'La marca no puede ser de menos de 3 letras'), django.core.validators.MaxLengthValidator(10, 'La marca no puede ser de más de 10 letras')])),
                ('modelo', models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(3, 'El modelo no puede ser de menos de 3 letras'), django.core.validators.MaxLengthValidator(30, 'El modelo no puede ser de más de 30 letras')])),
                ('cuerdas', models.IntegerField(validators=[django.core.validators.MinValueValidator(6, 'No pueden ser menos de 6 cuerdas'), django.core.validators.MaxValueValidator(12, 'No pueden ser más de 12 cuerdas')])),
                ('madera', models.CharField(default='No informada', max_length=50)),
                ('fecha_compra', models.DateField(validators=[formularios.models.validar_fecha])),
            ],
        ),
    ]
