from django.db import models


class Rooms(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название комнаты")
    description = models.TextField(verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена за ночь")
    quantity = models.PositiveIntegerField(verbose_name="Количество номеров")

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"

    def __str__(self):
        return f"Комната: {self.name} | Цена: {self.price} руб."
