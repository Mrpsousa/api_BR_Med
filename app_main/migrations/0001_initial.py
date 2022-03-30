# Generated by Django 4.0.3 on 2022-03-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado')),
                ('euro_dol', models.FloatField(default=0.0, verbose_name='euro-dolar')),
                ('brl_dol', models.FloatField(default=0.0, verbose_name='real-dolar')),
                ('jpy_dol', models.FloatField(default=0.0, verbose_name='iene-dolar')),
            ],
            options={
                'verbose_name': 'Valor',
                'verbose_name_plural': 'Valores',
            },
        ),
    ]