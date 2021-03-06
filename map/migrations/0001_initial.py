# Generated by Django 3.2.13 on 2022-05-03 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0005_announcement_estimate_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('area', models.FloatField()),
                ('facility_type', models.CharField(max_length=32, null=True)),
            ],
            options={
                'db_table': 'Facility',
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('facility_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='map.facility')),
                ('name', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=20)),
                ('county', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('number1', models.CharField(max_length=20)),
                ('number2', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Building',
            },
            bases=('map.facility', models.Model),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board')),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.facility')),
            ],
            options={
                'db_table': 'Business',
            },
        ),
    ]
