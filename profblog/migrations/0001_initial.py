# Generated by Django 5.1 on 2024-08-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='c',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='e',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='h',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='m',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='mh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='t',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.TextField()),
            ],
        ),
    ]
