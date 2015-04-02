# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                # ('Meal'), models.
                ('description', models.TextField(help_text=b'This is a quick description of your recipe', null=True, blank=True)),
                ('directions', models.TextField(help_text=b'How to make the recipe')),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient')),
                # ('comments'), models.ManyToOneRel(to='recipes.Comment')
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
