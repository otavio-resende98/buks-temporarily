# Generated by Django 2.2.6 on 2019-11-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cpf', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='CPF')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('data_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('email', models.EmailField(max_length=255, verbose_name='E-Mail')),
                ('celular', models.CharField(max_length=255, verbose_name='Celular')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
