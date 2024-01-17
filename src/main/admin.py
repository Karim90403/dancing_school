from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from main.models.choreographer import Сhoreographer
from main.models.client import Client
from main.models.client_record import ClientRecord
from main.models.dance_group import DanceGroup
from main.models.group_member import GroupMember
from main.models.item import Item
from main.models.sale import Sale
from main.models.shedule import Schedule
from main.models.subscription import Subscription
from main.models.test_class import TestClass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "fio", "birthday", "gender", "phone")
    search_fields = ["id", "fio"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "price", "name", "remaining", "availability")
    search_fields = ["id", "name"]


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "item_name", "client_name", "count_sold", "sale_date")
    search_fields = ["id", "item_name", "client_name", "sale_date"]

    def save_model(self, request, obj, form, change):
        if obj.save() == 0:
            messages.add_message(request, messages.ERROR, "К сожалению товар закончился")
        super(SaleAdmin, self).save_model(request, obj, form, change)

    @staticmethod
    @admin.display(description="Название товара")
    def item_name(sale_object):
        return mark_safe(sale_object.item.__str__())

    @staticmethod
    @admin.display(description="Имя клиента")
    def client_name(sale_object):
        return mark_safe(sale_object.client.__str__())


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("id", "group_name", "class_date", "class_time")
    search_fields = ["id", "group_name", "class_date", "class_time"]

    @staticmethod
    @admin.display(description="Название группы")
    def group_name(sale_object):
        return mark_safe(sale_object.group.__str__())


@admin.register(Сhoreographer)
class ChoreographerAdmin(admin.ModelAdmin):
    list_display = ("id", "fio", "birthday", "gender", "phone", "stage", "dance_style")
    search_fields = ["id", "fio", "dance_style"]


@admin.register(DanceGroup)
class DanceGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "choreographer", "dance_style")
    search_fields = ["id", "choreographer", "dance_style"]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "client_name", "lessons_left", "summ_lessons", "start_date", "end_date", "status")
    search_fields = ["id", "client_name", "start_date", "end_date", "status"]

    def save_model(self, request, obj, form, change):
        if obj.save() == "time":
            messages.add_message(request, messages.ERROR, "Время начала больше чем время окончания!")
        elif obj.save() == "number":
            messages.add_message(request, messages.ERROR, "Сумма оставшихся занятий больше изначальной суммы!")
        super(SubscriptionAdmin, self).save_model(request, obj, form, change)

    @staticmethod
    @admin.display(description="Имя клиента")
    def client_name(sale_object):
        return mark_safe(sale_object.client.__str__())


@admin.register(TestClass)
class TestClassAdmin(admin.ModelAdmin):
    list_display = ("id", "choreographer_name", "class_date", "class_time")
    search_fields = ["id", "choreographer_name", "class_date", "class_time"]

    @staticmethod
    @admin.display(description="Имя хореографа")
    def choreographer_name(sale_object):
        return mark_safe(sale_object.choreographer.__str__())


@admin.register(ClientRecord)
class ClientRecordAdmin(admin.ModelAdmin):
    list_display = ("test_class", "client")

    def save_model(self, request, obj, form, change):
        if obj.save() == 0:
            messages.add_message(request, messages.ERROR, "Клиент уже имеет запись на это время")
        super(ClientRecordAdmin, self).save_model(request, obj, form, change)


@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ("group", "client")
