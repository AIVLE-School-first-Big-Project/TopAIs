# Generated by Django 4.0.4 on 2022-04-28 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=128)),
                ('phone', models.CharField(max_length=16)),
                ('user_type', models.CharField(choices=[('Company', 0), ('Agency', 1)], max_length=32)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('area', models.CharField(max_length=32)),
                ('email_auth', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Agency',
            },
            bases=('accounts.user', models.Model),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('uid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('comp_category', models.CharField(choices=[('Cool-Roof', 0), ('Road-Line', 1)], max_length=32)),
                ('comp_name', models.CharField(max_length=32)),
                ('comp_homepage', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'Company',
            },
            bases=('accounts.user', models.Model),
        ),
    ]
