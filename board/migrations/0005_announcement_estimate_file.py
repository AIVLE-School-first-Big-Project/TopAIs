# Generated by Django 3.2.13 on 2022-05-03 07:43

import board.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_board_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('uploadFile', models.FileField(upload_to=board.models.get_file_path)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'File',
            },
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='board.file')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board')),
            ],
            options={
                'db_table': 'Estimate',
            },
            bases=('board.file',),
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='board.file')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board')),
            ],
            options={
                'db_table': 'Announcement',
            },
            bases=('board.file',),
        ),
    ]