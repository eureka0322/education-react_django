# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 06:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_light_enums.db
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22)),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Position')),
                ('object_id', models.PositiveIntegerField()),
                ('is_correct', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['position'],
                'db_table': 'curricula_answers',
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('published_on', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'curricula',
                'db_table': 'curricula_curricula',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22)),
                ('name', models.CharField(max_length=200)),
                ('published_on', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
                ('image', models.ImageField(upload_to='')),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Position')),
            ],
            options={
                'ordering': ['position'],
                'db_table': 'curricula_lessons',
            },
        ),
        migrations.CreateModel(
            name='LessonProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('score', models.SmallIntegerField(default=0)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='curricula.Lesson')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_progress', to='profiles.Profile')),
            ],
            options={
                'db_table': 'curricula_lesson_progress',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22)),
                ('name', models.CharField(max_length=200)),
                ('published_on', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
                ('image', models.ImageField(upload_to='')),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Position')),
            ],
            options={
                'ordering': ['position'],
                'db_table': 'curricula_modules',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22)),
                ('text', models.CharField(max_length=200)),
                ('published_on', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('question_type', django_light_enums.db.EnumField(choices=[(10, 'SINGLE_ANSWER'), (20, 'MULTIPLE_CHOICE')], default=10, enum_values=(10, 20))),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Position')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='curricula.Lesson')),
            ],
            options={
                'ordering': ['position'],
                'db_table': 'curricula_questions',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'curricula_texts',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22)),
                ('name', models.CharField(max_length=200)),
                ('published_on', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Position')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='curricula.Curriculum')),
            ],
            options={
                'ordering': ['position'],
                'db_table': 'curricula_units',
            },
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField()),
                ('is_correct', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='profiles.Profile')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='curricula.Question')),
            ],
            options={
                'db_table': 'curricula_user_responses',
            },
        ),
        migrations.CreateModel(
            name='Vector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('magnitude', models.FloatField(blank=True, null=True, verbose_name='Magnitude')),
                ('angle', models.FloatField(blank=True, null=True, verbose_name='Angle')),
                ('x_component', models.FloatField(blank=True, null=True, verbose_name='x-Component')),
                ('y_component', models.FloatField(blank=True, null=True, verbose_name='y-Component')),
            ],
            options={
                'db_table': 'curricula_vectors',
            },
        ),
        migrations.AddField(
            model_name='module',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='curricula.Unit'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='curricula.Module'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='curricula.Question'),
        ),
    ]
