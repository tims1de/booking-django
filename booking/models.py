from django.db import models

from rooms.models import Rooms
from users.models import Users


class Bookings(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="bookings")
    rooms = models.ManyToManyField(Rooms, verbose_name="Номера")
    date_from = models.DateField(verbose_name="Дата начала")
    date_to = models.DateField(verbose_name="Дата окончания")
    price_per_day = models.PositiveIntegerField(editable=False, default=0, verbose_name="Цена за день")
    total_days = models.PositiveIntegerField(editable=False, default=0, verbose_name="Всего дней")
    total_price = models.PositiveIntegerField(editable=False, default=0, verbose_name="Итоговая цена бронирования")

    def save(self, *args, **kwargs):
        delta = self.date_to - self.date_from
        self.total_days = delta.days + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

    def __str__(self):
        room_names = ", ".join([room.name for room in self.rooms.all()])
        return f"Бронь {self.user} | Комнаты: {room_names} | {self.date_from} - {self.date_to} | Итоговая цена: {self.total_price}"
