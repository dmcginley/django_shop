# Generated by Django 4.1.1 on 2022-10-03 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="image_file",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
    ]