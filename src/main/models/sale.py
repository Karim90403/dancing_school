from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from main.models.item import StatusChoice
from main.models.mixins import IdMixin


class Sale(IdMixin):
    item = models.ForeignKey("Item", verbose_name="Товар", on_delete=models.CASCADE)
    client = models.ForeignKey("Client", verbose_name="Клиент", on_delete=models.CASCADE)
    count_sold = models.SmallIntegerField("Количество", validators=[MinValueValidator(1)])
    sale_date = models.DateField("Дата продажи", auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        try:
            old_instance: Sale = Sale.objects.get(id=self.id)
            self.item.remaining = self.item.remaining + old_instance.count_sold
        except Sale.DoesNotExist:  # to handle initial object creation
            pass
        finally:
            if self.item.remaining >= self.count_sold:
                self.item.remaining = self.item.remaining - self.count_sold
            else:
                self.count_sold = self.item.remaining
                self.item.remaining = 0
                self.item.availability = StatusChoice.NO
            self.item.save()
        if self.item.remaining == 0:
            return 0
        else:
            super(Sale, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"
