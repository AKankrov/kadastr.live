# Generated by Django 3.1.4 on 2023-05-10 15:02

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0002_auto_20230510_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='georecord',
            name='geometry_zoom_10',
            field=django.contrib.gis.db.models.fields.GeometryField(default=None, srid=4326),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='georecord',
            name='geometry_zoom_12',
            field=django.contrib.gis.db.models.fields.GeometryField(default=None, srid=4326),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='georecord',
            name='geometry_zoom_8',
            field=django.contrib.gis.db.models.fields.GeometryField(default=None, srid=4326),
            preserve_default=False,
        ),
    ]
