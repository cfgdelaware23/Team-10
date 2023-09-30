# Generated by Django 4.2.2 on 2023-09-29 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="events",
            name="time",
        ),
        migrations.AddField(
            model_name="events",
            name="broadcaster",
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name="events",
            name="end_time",
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name="events",
            name="facilitator",
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name="events",
            name="moderator",
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name="events",
            name="start_time",
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name="events",
            name="account",
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name="events",
            name="day",
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name="events",
            name="host",
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name="events",
            name="recurring",
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name="events",
            name="title",
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="day",
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="name",
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="roles",
            field=models.TextField(default=None),
        ),
    ]
