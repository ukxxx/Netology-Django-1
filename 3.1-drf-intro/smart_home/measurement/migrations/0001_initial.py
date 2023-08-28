# Generated by Django 4.2.3 on 2023-08-23 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sensor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Measurement",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("temperature", models.DecimalField(decimal_places=2, max_digits=5)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("time", models.TimeField(auto_now_add=True)),
                (
                    "sensor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="measurement.sensor",
                    ),
                ),
            ],
        ),
    ]
