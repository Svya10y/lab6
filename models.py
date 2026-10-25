from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField("Название задания", max_length=200)
    client = models.CharField("Клиент", max_length=200)
    contact = models.CharField("Контактное лицо", max_length=200)
    department = models.CharField("Отдел", max_length=200)
    employee = models.CharField("Сотрудник", max_length=200)
    issue_date = models.DateField("Дата выдачи")
    hours = models.IntegerField("Трудоемкость, ч")
    hour_rate = models.DecimalField("Стоимость часа, руб.", max_digits=10, decimal_places=2)
    discount = models.DecimalField("Скидка, %", max_digits=10, decimal_places=2)
    text = models.TextField("Описание задания")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор записи")
    created_date = models.DateField("Дата создания записи", auto_now_add=True)

    class Meta:
        verbose_name = "задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return "%s: %s" % (self.client, self.title)

    def get_excerpt(self):
        return self.text[:140] + "..." if len(self.text) > 140 else self.text

    def get_cost(self):
        # стоимость задания = трудоемкость * стоимость часа с учетом скидки постоянного клиента
        return round(self.hours * self.hour_rate * (100 - self.discount) / 100, 2)
