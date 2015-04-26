# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20141004_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(upload_to=b'%Y/%m/%d'),
        ),
    ]
