# Generated by Django 3.1.1 on 2020-09-03 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20200903_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.TimeField(auto_now_add=True)),
                ('updated', models.TimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.TimeField(auto_now_add=True)),
                ('updated', models.TimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HouseRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.TimeField(auto_now_add=True)),
                ('updated', models.TimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='room',
            name='roomtype',
        ),
        migrations.AddField(
            model_name='room',
            name='roomtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.roomtype'),
        ),
        migrations.AddField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(blank=True, to='rooms.Amenity'),
        ),
        migrations.AddField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(blank=True, to='rooms.Facility'),
        ),
        migrations.AddField(
            model_name='room',
            name='house_rules',
            field=models.ManyToManyField(blank=True, to='rooms.HouseRule'),
        ),
    ]
