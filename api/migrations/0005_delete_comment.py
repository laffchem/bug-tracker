# Generated by Django 4.1.6 on 2023-02-13 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_bug_status"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Comment",
        ),
    ]