from django.contrib.auth.hashers import make_password
from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=255, unique=True, verbose_name="Имя пользователя")
    password = models.CharField(max_length=128, verbose_name="Пароль пользователя")

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"