# Generated by Django 4.2.5 on 2023-12-06 22:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('fio', models.CharField(max_length=90, verbose_name='fio')),
                ('birthday', models.DateField(verbose_name='birthday')),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, verbose_name='gender')),
                ('phone', models.BigIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(111111)], verbose_name='phone')),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
            },
        ),
        migrations.CreateModel(
            name='DanceGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('dance_style', models.CharField(max_length=30, verbose_name='dance_style')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='price')),
                ('remaining', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='remaining')),
                ('availability', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=3, verbose_name='availability')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
        migrations.CreateModel(
            name='Сhoreographer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('fio', models.CharField(max_length=90, verbose_name='fio')),
                ('birthday', models.DateField(verbose_name='birthday')),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, verbose_name='gender')),
                ('phone', models.BigIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(111111)], verbose_name='phone')),
                ('stage', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='stage')),
                ('dance_style', models.CharField(max_length=30, verbose_name='dance_style')),
            ],
            options={
                'verbose_name': 'choreographer',
                'verbose_name_plural': 'choreographers',
            },
        ),
        migrations.CreateModel(
            name='TestClass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('class_date', models.DateField(verbose_name='class_date')),
                ('class_time', models.TimeField(verbose_name='class_time')),
                ('choreographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.сhoreographer', verbose_name='choreographer')),
            ],
            options={
                'verbose_name': 'test_class',
                'verbose_name_plural': 'test_classes',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('lessons_left', models.SmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='lessons_left')),
                ('summ_lessons', models.SmallIntegerField(default=10, validators=[django.core.validators.MinValueValidator(1)], verbose_name='summ_lessons')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='start_date')),
                ('end_date', models.DateField(verbose_name='end_date')),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('SUSPENDED', 'Suspended')], default='ACTIVE', max_length=10, verbose_name='subscription_status')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client', verbose_name='client')),
            ],
            options={
                'verbose_name': 'subscription',
                'verbose_name_plural': 'subscriptions',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('class_date', models.DateField(verbose_name='class_date')),
                ('class_time', models.TimeField(verbose_name='class_time')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dancegroup', verbose_name='group')),
            ],
            options={
                'verbose_name': 'schedule',
                'verbose_name_plural': 'schedules',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('count_sold', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='count_sold')),
                ('sale_date', models.DateField(auto_now_add=True, verbose_name='sale_date')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client', verbose_name='client')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item', verbose_name='item')),
            ],
            options={
                'verbose_name': 'sale',
                'verbose_name_plural': 'sales',
            },
        ),
        migrations.AddField(
            model_name='dancegroup',
            name='choreographer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.сhoreographer', verbose_name='choreographer'),
        ),
        migrations.AddField(
            model_name='dancegroup',
            name='members',
            field=models.ManyToManyField(related_name='group', to='main.client', verbose_name='members'),
        ),
        migrations.AddField(
            model_name='client',
            name='records',
            field=models.ManyToManyField(related_name='record', to='main.schedule', verbose_name='records'),
        ),
    ]
