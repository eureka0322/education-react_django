# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-07 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django_light_enums.db


class Migration(migrations.Migration):

    dependencies = [
        ('curricula', '0011_auto_20170521_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonprogress',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_type',
            field=django_light_enums.db.EnumField(choices=[(0, 'DEFAULT'), (1, 'GAME')], default=0, enum_values=(0, 1)),
        ),
        migrations.AlterField(
            model_name='lessonprogress',
            name='status',
            field=django_light_enums.db.EnumField(choices=[(0, 'LOCKED'), (10, 'NEW'), (20, 'UNLOCKED'), (30, 'COMPLETE')], default=0, enum_values=(0, 10, 20, 30)),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_type',
            field=django_light_enums.db.EnumField(choices=[(0, 'UNDEFINED'), (50, 'MATHEMATICAL_EXPRESSION'), (20, 'VECTOR'), (40, 'IMAGE'), (10, 'TEXT'), (60, 'VECTOR_COMPONENTS'), (30, 'NULLABLE_VECTOR')], default=0, enum_values=(0, 50, 20, 40, 10, 60, 30)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=django_light_enums.db.EnumField(choices=[(0, 'UNDEFINED'), (10, 'SINGLE_ANSWER'), (20, 'MULTIPLE_CHOICE')], default=0, enum_values=(0, 10, 20)),
        ),
    ]
