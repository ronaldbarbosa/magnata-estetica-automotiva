# Generated by Django 4.2 on 2023-04-21 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('assunto', models.CharField(max_length=50)),
                ('mensagem', models.CharField(max_length=300)),
            ],
        ),
    ]
