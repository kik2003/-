# Generated by Django 3.2.8 on 2022-06-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiHome', '0002_auto_20220624_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.DateTimeField(verbose_name='запис'),
        ),
    ]