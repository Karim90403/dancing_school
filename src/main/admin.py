from main.models.client import Client
from main.models.item import Item
from main.models.sale import Sale
from main.models.shedule import Schedule
from main.models.choreographer import Сhoreographer
from main.models.dance_group import DanceGroup
from main.models.subscription import Subscription
from main.models.test_class import TestClass
from django.contrib import admin
from django.utils.safestring import mark_safe


@admin.register(Client)
class ProtocolAdmin(admin.ModelAdmin):
    filter_horizontal = ("records",)
    list_display = ("id", "fio", "birthday", "gender", "phone")


@admin.register(Item)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ("id", "price", "name", "remaining", "availability")


@admin.register(Sale)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ("id", "item_name", "client_name", "count_sold", "sale_date")

    @staticmethod
    def item_name(sale_object):
        return mark_safe(sale_object.item.__str__())

    @staticmethod
    def client_name(sale_object):
        return mark_safe(sale_object.client.__str__())


@admin.register(Schedule)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ("id", "group_id", "class_date", "class_time")


@admin.register(Сhoreographer)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ("id", "fio", "birthday", "gender", "phone", "stage", "dance_style")


@admin.register(DanceGroup)
class ProtocolAdmin(admin.ModelAdmin):
    filter_horizontal = ("members",)
    list_display = ("id", "choreographer", "dance_style")


@admin.register(Subscription)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ("id", "client_name", "lessons_left", "summ_lessons", "start_date", "end_date", "status")

    @staticmethod
    def client_name(sale_object):
        return mark_safe(sale_object.client.__str__())


@admin.register(TestClass)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ("id", "choreographer_name", "class_date", "class_time")

    @staticmethod
    def choreographer_name(sale_object):
        return mark_safe(sale_object.choreographer.__str__())
