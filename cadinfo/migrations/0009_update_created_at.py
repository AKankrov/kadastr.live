# Generated by Django 3.1.4 on 2022-01-20 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cadinfo', '0008_remove_update_latest_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
