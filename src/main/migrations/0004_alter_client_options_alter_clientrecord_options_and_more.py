# Generated by Django 4.2.5 on 2024-01-05 13:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_remove_client_records_remove_dancegroup_members_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={"verbose_name": "Клиент", "verbose_name_plural": "Клиенты"},
        ),
        migrations.AlterModelOptions(
            name="clientrecord",
            options={
                "verbose_name": "Запись клиента",
                "verbose_name_plural": "Записи клиентов",
            },
        ),
        migrations.AlterModelOptions(
            name="dancegroup",
            options={"verbose_name": "Группа", "verbose_name_plural": "Группы"},
        ),
        migrations.AlterModelOptions(
            name="groupmember",
            options={
                "verbose_name": "Участник группы",
                "verbose_name_plural": "Участники группы",
            },
        ),
        migrations.AlterModelOptions(
            name="item",
            options={"verbose_name": "Товар", "verbose_name_plural": "Товары"},
        ),
        migrations.AlterModelOptions(
            name="sale",
            options={"verbose_name": "Продажа", "verbose_name_plural": "Продажи"},
        ),
        migrations.AlterModelOptions(
            name="schedule",
            options={"verbose_name": "Расписание", "verbose_name_plural": "Расписания"},
        ),
        migrations.AlterModelOptions(
            name="subscription",
            options={"verbose_name": "Абонемент", "verbose_name_plural": "Абонементы"},
        ),
        migrations.AlterModelOptions(
            name="testclass",
            options={
                "verbose_name": "Пробное занятие",
                "verbose_name_plural": "Пробные занятия",
            },
        ),
        migrations.AlterModelOptions(
            name="сhoreographer",
            options={"verbose_name": "Хореограф", "verbose_name_plural": "Хореографы"},
        ),
        migrations.AlterField(
            model_name="client",
            name="birthday",
            field=models.DateField(verbose_name="Дата рождения"),
        ),
        migrations.AlterField(
            model_name="client",
            name="fio",
            field=models.CharField(max_length=90, verbose_name="Фио"),
        ),
        migrations.AlterField(
            model_name="client",
            name="gender",
            field=models.CharField(
                choices=[("M", "М"), ("F", "Ж")], max_length=1, verbose_name="Пол"
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="phone",
            field=models.BigIntegerField(
                unique=True,
                validators=[django.core.validators.MinValueValidator(111111)],
                verbose_name="Номер телефона",
            ),
        ),
        migrations.AlterField(
            model_name="clientrecord",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="main.client",
                verbose_name="Клиент",
            ),
        ),
        migrations.AlterField(
            model_name="clientrecord",
            name="test_class",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="main.testclass",
                verbose_name="Пробное занятие",
            ),
        ),
        migrations.AlterField(
            model_name="dancegroup",
            name="choreographer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="main.сhoreographer",
                verbose_name="Хореограф",
            ),
        ),
        migrations.AlterField(
            model_name="dancegroup",
            name="dance_style",
            field=models.CharField(max_length=30, verbose_name="Стиль танцев"),
        ),
        migrations.AlterField(
            model_name="groupmember",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="main.client",
                verbose_name="Клиент",
            ),
        ),
        migrations.AlterField(
            model_name="groupmember",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="main.dancegroup",
                verbose_name="Группа",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="availability",
            field=models.CharField(
                choices=[("Yes", "Да"), ("No", "Нет")],
                max_length=3,
                verbose_name="Наличие",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(max_length=30, verbose_name="Название товара"),
        ),
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Цена",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="remaining",
            field=models.SmallIntegerField(
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Осталось",
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="main.client",
                verbose_name="Клиент",
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="count_sold",
            field=models.SmallIntegerField(
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Количество",
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="main.item",
                verbose_name="Товар",
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="sale_date",
            field=models.DateField(auto_now_add=True, verbose_name="Дата продажи"),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="class_date",
            field=models.DateField(verbose_name="Дата занятия"),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="class_time",
            field=models.TimeField(verbose_name="Время занятия"),
        ),
        migrations.AlterField(
            model_name="schedule",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="main.dancegroup",
                verbose_name="Группа",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="main.client",
                verbose_name="Клиент",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="end_date",
            field=models.DateField(verbose_name="Дата конца"),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="lessons_left",
            field=models.SmallIntegerField(
                null=True,
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Прошло занятий",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="start_date",
            field=models.DateField(verbose_name="Дата начала"),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="status",
            field=models.CharField(
                choices=[("ACTIVE", "Активен"), ("SUSPENDED", "Закончен")],
                default="ACTIVE",
                max_length=10,
                verbose_name="Статус абоенемента",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="summ_lessons",
            field=models.SmallIntegerField(
                default=10,
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Всего зантий",
            ),
        ),
        migrations.AlterField(
            model_name="testclass",
            name="choreographer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="main.сhoreographer",
                verbose_name="Хореограф",
            ),
        ),
        migrations.AlterField(
            model_name="testclass",
            name="class_date",
            field=models.DateField(verbose_name="Дата занятия"),
        ),
        migrations.AlterField(
            model_name="testclass",
            name="class_time",
            field=models.TimeField(verbose_name="Время занятия"),
        ),
        migrations.AlterField(
            model_name="сhoreographer",
            name="birthday",
            field=models.DateField(verbose_name="Дата рождения"),
        ),
        migrations.AlterField(
            model_name="сhoreographer",
            name="dance_style",
            field=models.CharField(max_length=30, verbose_name="Стиль танцев"),
        ),
        migrations.AlterField(
            model_name="сhoreographer",
            name="fio",
            field=models.CharField(max_length=90, verbose_name="ФИО"),
        ),
        migrations.AlterField(
            model_name="сhoreographer",
            name="gender",
            field=models.CharField(
                choices=[("M", "М"), ("F", "Ж")], max_length=1, verbose_name="Пол"
            ),
        ),
        migrations.AlterField(
            model_name="сhoreographer",
            name="phone",
            field=models.BigIntegerField(
                unique=True,
                validators=[django.core.validators.MinValueValidator(111111)],
                verbose_name="Номер телефона",
            ),
        ),
        migrations.AlterField(
            model_name="сhoreographer",
            name="stage",
            field=models.SmallIntegerField(
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Стаж",
            ),
        ),
    ]