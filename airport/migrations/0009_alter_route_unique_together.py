# Generated by Django 5.1.4 on 2024-12-13 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("airport", "0008_airplanetype_image_airport_image"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="route",
            unique_together={("source", "destination")},
        ),
    ]
