# Generated by Django 4.1.1 on 2022-10-02 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=254)),
                ("title", models.CharField(max_length=254)),
                ("authors", models.CharField(max_length=254)),
                (
                    "main_picture_medium",
                    models.URLField(blank=True, max_length=1024, null=True),
                ),
                (
                    "main_picture_large",
                    models.URLField(blank=True, max_length=1024, null=True),
                ),
                (
                    "alternative_titles_en",
                    models.CharField(blank=True, max_length=254, null=True),
                ),
                (
                    "alternative_titles_ja",
                    models.CharField(blank=True, max_length=254, null=True),
                ),
                ("synopsis", models.TextField()),
                ("mean", models.CharField(max_length=254)),
                ("genres", models.CharField(max_length=254)),
            ],
        ),
    ]
