# Generated by Django 3.2.8 on 2022-06-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiHome', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': 'Запис', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterField(
            model_name='record',
            name='number',
            field=models.CharField(max_length=10, verbose_name='номер'),
        ),
    ]
