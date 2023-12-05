# Generated by Django 4.2.7 on 2023-12-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(default="", max_length=40, unique=True)),
                ("summary", models.CharField(default="", max_length=100)),
                ("designation", models.CharField(default="", max_length=40)),
            ],
            options={
                "db_table": "employee",
            },
        ),
        migrations.CreateModel(
            name="Person",
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
                ("username", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=30)),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]