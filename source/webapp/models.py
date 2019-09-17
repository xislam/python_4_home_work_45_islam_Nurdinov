from django.db import models

status_choices = [('new', 'новый'), ('in_progress', 'в прецесе'), ('done', 'завершена')]


class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст')
    date = models.DateField(max_length=3000, null=True, blank=True, verbose_name='Дата')
    status = models.CharField(max_length=20, verbose_name='Тема', default=status_choices[0][0], choices=status_choices)

    def __str__(self):
        return self.description
