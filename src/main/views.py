import datetime

from django.db.models import Count
from django.shortcuts import render
from main.models.choreographer import Сhoreographer
from main.models.dance_group import DanceGroup
from main.models.group_member import GroupMember
from main.models.shedule import Schedule
from main.models.test_class import TestClass


def index(request):
    return render(request, "index.html")


def groups_schedule(request):
    schedules = []
    group_ids = []
    search_query = request.GET.get("search_box", None)
    try:
        search_date = datetime.datetime.strptime(search_query, "%d-%m-%Y").date()
        return render(
            request, "schedule.html", {"data": Schedule.objects.filter(class_date=search_date).order_by("group")}
        )
    except (TypeError, ValueError):
        pass
    for group in DanceGroup.objects.filter(dance_style=search_query):
        group_ids.append(group.id)
    for choreographer in Сhoreographer.objects.filter(fio=search_query):
        for group in DanceGroup.objects.filter(choreographer=choreographer.id):
            group_ids.append(group.id)
    for group_id in set(group_ids):
        for schedule in Schedule.objects.filter(group=group_id, class_date__gt=datetime.date.today()).order_by("group"):
            schedules.append(schedule)
    if not search_query:
        return render(
            request,
            "schedule.html",
            {"data": Schedule.objects.filter(class_date__gt=datetime.date.today()).order_by("group")},
        )
    return render(request, "schedule.html", {"data": schedules})


def test_classes(request):
    classes = []
    choreographer_ids = []
    search_query = request.GET.get("search_box", None)
    try:
        search_date = datetime.datetime.strptime(search_query, "%d-%m-%Y").date()
        return render(
            request,
            "test_class.html",
            {
                "data": TestClass.objects.annotate(number_of_classes=Count("clientrecord"))
                .filter(class_date=search_date)
                .order_by("choreographer")
            },
        )
    except (TypeError, ValueError) as e:
        print(e)
        pass
    for choreographer in Сhoreographer.objects.filter(fio=search_query):
        choreographer_ids.append(choreographer.id)
    for choreographer in Сhoreographer.objects.filter(dance_style=search_query):
        choreographer_ids.append(choreographer.id)
    for choreographer_id in set(choreographer_ids):
        for schedule in (
            TestClass.objects.annotate(number_of_classes=Count("clientrecord"))
            .filter(choreographer=choreographer_id, class_date__gt=datetime.date.today())
            .order_by("choreographer")
        ):
            classes.append(schedule)
    if not search_query:
        return render(
            request,
            "test_class.html",
            {
                "data": TestClass.objects.annotate(number_of_classes=Count("clientrecord"))
                .filter(class_date__gt=datetime.date.today())
                .order_by("choreographer")
            },
        )
    return render(request, "test_class.html", {"data": classes})


def groups_list(request):
    members = []
    group_ids = []
    search_query = request.GET.get("search_box", None)
    for group in DanceGroup.objects.filter(dance_style=search_query):
        group_ids.append(group.id)
    for choreographer in Сhoreographer.objects.filter(fio=search_query):
        for group in DanceGroup.objects.filter(choreographer=choreographer.id):
            group_ids.append(group.id)
    for group_id in set(group_ids):
        for schedule in GroupMember.objects.filter(group=group_id).order_by("group"):
            members.append(schedule)
    if not search_query:
        return render(request, "members.html", {"data": GroupMember.objects.all().order_by("group")})
    return render(request, "members.html", {"data": members})
