from django.db import models
from main.models.test_class import TestClass


class ClientRecord(models.Model):
    test_class = models.ForeignKey("TestClass", verbose_name="Пробное занятие", on_delete=models.CASCADE)
    client = models.ForeignKey("Client", verbose_name="Клиент", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.client) + str(self.test_class)

    def save(self, *args, **kwargs):
        test_classes = TestClass.objects.all().filter(
            class_date=self.test_class.class_date, class_time=self.test_class.class_time
        )
        for test_class in test_classes:
            if test_class != self.test_class:
                try:
                    ClientRecord.objects.all().filter(test_class=test_class, client=self.client)
                    return 0
                except Exception:
                    pass
        super(ClientRecord, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Запись клиента"
        verbose_name_plural = "Записи клиентов"
        unique_together = (
            "test_class",
            "client",
        )
