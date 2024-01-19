# Generated by Django 4.2.5 on 2024-01-19 22:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_alter_client_options_alter_clientrecord_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="remaining",
            field=models.SmallIntegerField(
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Осталось",
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="count_sold",
            field=models.SmallIntegerField(
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Количество",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="clientrecord",
            unique_together={("test_class", "client")},
        ),
        migrations.AlterUniqueTogether(
            name="schedule",
            unique_together={("group", "class_date", "class_time")},
        ),
        migrations.AlterUniqueTogether(
            name="testclass",
            unique_together={("choreographer", "class_date", "class_time")},
        ),
    ]
