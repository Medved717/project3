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


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название автомобиля',
                             help_text='Введите название автомобиля.')
    description = models.TextField(verbose_name='Описание автомобиля', help_text='Введите описание автомобиля.')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ('title',)

    def __str__(self):
        return self.title

class Mileage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, blank=True, null=True)

    mileage = models.PositiveIntegerField(verbose_name='Пробег')
    year = models.PositiveSmallIntegerField(max_length=4, verbose_name='Год регистрации')

    def __str__(self):
        return f'{self.moto if self.moto else self.car} - {self.year}'

    class Meta:
        verbose_name = 'Пробег'
        verbose_name_plural = 'Пробег'
        ordering = ('-year',)