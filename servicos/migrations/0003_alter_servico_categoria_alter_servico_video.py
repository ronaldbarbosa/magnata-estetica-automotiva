# Generated by Django 4.2 on 2023-06-09 22:51

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_alter_servico_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='categoria',
            field=models.CharField(choices=[('SIMPLES', 'Simples'), ('DETALHADO', 'Detalhado')], max_length=10),
        ),
        migrations.AlterField(
            model_name='servico',
            name='video',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]
