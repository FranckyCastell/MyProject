# Generated by Django 3.2.9 on 2021-11-10 17:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_auto_20211110_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=500, verbose_name='Descripción'),
            preserve_default=False,
        ),
    ]
