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
        if self.item.remaining == 0:
            return 0
        else:
            super(Sale, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"


@receiver(pre_save, sender=Sale, dispatch_uid="create_sale")
def create_stock(sender, instance, **kwargs):
    try:
        old_instance = Sale.objects.get(id=instance.id)
        instance.item.remaining = instance.item.remaining + old_instance.count_sold
    except Sale.DoesNotExist:  # to handle initial object creation
        pass
    finally:
        if instance.item.remaining >= instance.count_sold:
            instance.item.remaining = instance.item.remaining - instance.count_sold
        else:
            instance.count_sold = instance.item.remaining
            instance.item.remaining = 0
            instance.item.availability = StatusChoice.NO
        instance.item.save()
