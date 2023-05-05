# Generated by Django 4.1.7 on 2023-03-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("docfile", models.FileField(upload_to="documents/%Y/%m/%d")),
            ],
        ),
    ]