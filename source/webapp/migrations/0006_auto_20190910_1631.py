# Generated by Django 2.2.4 on 2019-09-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20190909_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='text',
            field=models.TextField(default='', max_length=3000, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default='', max_length=3000, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(default='', max_length=200, verbose_name='Описание'),
        ),
    ]
