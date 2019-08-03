from django.db import models
from workers.models import Departaments
from django.conf import settings

class Position(models.Model):
    name=models.CharField(max_length=255,verbose_name='Должнотость')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должность'

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='Пользыватель')
    departament=models.ForeignKey(Departaments,on_delete=models.CASCADE,verbose_name='Департамент')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')
    class Meta:
        verbose_name_plural='Пользыватель'
        verbose_name='Пользыватель'