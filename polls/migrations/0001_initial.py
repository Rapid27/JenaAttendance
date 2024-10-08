# Generated by Django 4.1.2 on 2023-03-31 22:28

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
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("surname", models.CharField(max_length=255)),
                (
                    "Department",
                    models.CharField(
                        choices=[
                            ("1", "Mining"),
                            ("2", "Engineering"),
                            ("3", "adminstration"),
                        ],
                        default="1",
                        max_length=2,
                    ),
                ),
                ("phone_number", models.IntegerField(default=222)),
                ("mine_number", models.IntegerField(default=222)),
            ],
            options={
                "db_table": "Employee",
            },
        ),
    ]
