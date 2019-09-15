from django.db import models

STATUS_CHOICES = [('new', 'New'), ('In progress', 'In progress'),  ('done', 'Done')]


class ToDoList(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=3000, null=False, blank=False, default=STATUS_CHOICES[0][0], verbose_name='Статус',
                              choices=STATUS_CHOICES)
    text = models.TextField(max_length=3000, null=True, blank=False, verbose_name='Подробное описание')
    done_at = models.DateField(verbose_name='Дата выполнения', null=True, blank=False)

    def __str__(self):
        return self.description
