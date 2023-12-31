# Generated by Django 4.2.5 on 2023-12-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("logic", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roommodel",
            name="current_connections",
            field=models.JSONField(
                blank=True,
                default=list,
                null=True,
                verbose_name="Lista de conexiones actuales",
            ),
        ),
    ]
