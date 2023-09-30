# Generated by Django 4.2.2 on 2023-09-30 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_remove_events_time_events_broadcaster_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="events",
            name="streamer",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="events",
            name="account",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name="events",
            name="broadcaster",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="events",
            name="facilitator",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="events",
            name="host",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name="events",
            name="moderator",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="events",
            name="title",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="day",
            field=models.DateField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="name",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name="volunteer",
            name="roles",
            field=models.CharField(default=None, max_length=255),
        ),
    ]
