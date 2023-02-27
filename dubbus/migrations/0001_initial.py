# Generated by Django 4.0.5 on 2022-08-10 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('description_code', models.CharField(blank=True, max_length=10, null=True)),
                ('conditions', models.CharField(blank=True, max_length=80, null=True)),
                ('weather_type', models.CharField(blank=True, max_length=2, null=True)),
                ('date_time', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'forecast',
            },
        ),
        migrations.CreateModel(
            name='Stops',
            fields=[
                ('stop_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('stop_name', models.CharField(blank=True, max_length=255, null=True)),
                ('stop_lat', models.FloatField(blank=True, null=True)),
                ('stop_long', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stops',
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('temperature', models.IntegerField(blank=True, null=True)),
                ('feels_like', models.IntegerField(blank=True, null=True)),
                ('time_stamp', models.DateTimeField(primary_key=True, serialize=False)),
                ('weather_icon', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'weather',
            },
        ),
        migrations.CreateModel(
            name='StopTimesUpdated',
            fields=[
                ('trip_id', models.CharField(max_length=255)),
                ('departure_time', models.CharField(max_length=30)),
                ('stop_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('stop_sequence', models.IntegerField(blank=True, null=True)),
                ('stop_headsign', models.CharField(blank=True, max_length=255, null=True)),
                ('route_id', models.CharField(blank=True, max_length=30, null=True)),
                ('service_id', models.CharField(blank=True, max_length=30, null=True)),
                ('trip_headsign', models.CharField(blank=True, max_length=255, null=True)),
                ('route_short_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'stop_times_updated',
                'unique_together': {('stop_id', 'trip_id')},
            },
        ),
        migrations.CreateModel(
            name='RoutesUpdated',
            fields=[
                ('trip_headsign', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('route_short_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'routes_updated',
                'unique_together': {('trip_headsign', 'route_short_name')},
            },
        ),
        migrations.CreateModel(
            name='RouteStops',
            fields=[
                ('stop_id', models.CharField(max_length=255)),
                ('trip_headsign', models.CharField(max_length=255)),
                ('route_short_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('stop_name', models.CharField(blank=True, max_length=255, null=True)),
                ('stop_lat', models.FloatField(blank=True, null=True)),
                ('stop_long', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'route_stops',
                'unique_together': {('route_short_name', 'trip_headsign', 'stop_id')},
            },
        ),
        migrations.CreateModel(
            name='FavouriteStops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('stop_id', models.CharField(max_length=300)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'favouritestops',
            },
        ),
        migrations.CreateModel(
            name='FavouriteRoutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('trip_headsign', models.CharField(max_length=300)),
                ('route_short_name', models.CharField(max_length=300)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'favouriteroutes',
            },
        ),
    ]
