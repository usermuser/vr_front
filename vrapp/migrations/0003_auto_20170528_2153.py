# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vrapp', '0002_auto_20170528_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='duration',
            field=models.DateTimeField(),
        ),
    ]
