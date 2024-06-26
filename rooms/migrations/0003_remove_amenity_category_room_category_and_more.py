# Generated by Django 5.0.4 on 2024-04-21 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
        ("rooms", "0002_amenity_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="amenity",
            name="category",
        ),
        migrations.AddField(
            model_name="room",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.category",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="amenities",
            field=models.ManyToManyField(to="rooms.amenity"),
        ),
    ]
