# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0066_rm_character_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='optimal_score_boundary',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='level',
            name='pass_score_boundary',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
