# Generated by Django 4.1.6 on 2023-02-13 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bug",
            name="status",
            field=models.CharField(
                choices=[
                    ("New", "New"),
                    ("In Progress", "In Progress"),
                    ("Fixed", "Fixed"),
                    ("Closed", "Closed"),
                ],
                default="new",
                max_length=20,
            ),
        ),
    ]
