# Generated by Django 4.1.7 on 2023-02-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("room", "0004_alter_room_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
