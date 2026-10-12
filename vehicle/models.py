from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ('title',)

    def __str__(self):
        return self.title


