# Generated by Django 3.1.4 on 2023-05-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geojsonupload',
            name='file',
        ),
        migrations.AddField(
            model_name='geojsonupload',
            name='content_hash',
            field=models.CharField(default=None, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='geojsonupload',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
