# Generated by Django 4.1.7 on 2023-02-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("room", "0003_alter_room_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
