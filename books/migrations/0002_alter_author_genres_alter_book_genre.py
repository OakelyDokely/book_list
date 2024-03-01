# Generated by Django 4.1 on 2024-02-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="genres",
            field=models.ManyToManyField(blank=True, null=True, to="books.genre"),
        ),
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.ManyToManyField(blank=True, null=True, to="books.genre"),
        ),
    ]
