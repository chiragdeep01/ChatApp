# Generated by Django 4.1.7 on 2023-02-26 11:01

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("room", "0002_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="name", unique=True
            ),
        ),
    ]
