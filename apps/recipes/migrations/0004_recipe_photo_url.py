# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo_url',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
