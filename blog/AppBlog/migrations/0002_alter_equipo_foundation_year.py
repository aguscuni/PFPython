# Generated by Django 4.1.1 on 2022-10-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppBlog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipo",
            name="foundation_year",
            field=models.IntegerField(),
        ),
    ]
