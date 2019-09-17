# Generated by Django 2.2 on 2019-09-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20190906_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('date', models.DateField(verbose_name='Дата')),
                ('status', models.CharField(choices=[('new', 'новый'), ('in_progress', 'в прецесе'), ('done', 'завершена')], default='new', max_length=20, verbose_name='Тема')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]