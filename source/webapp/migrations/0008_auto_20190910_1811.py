# Generated by Django 2.2.4 on 2019-09-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20190910_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, max_length=3000, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Текст'),
        ),
    ]