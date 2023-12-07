# Generated by Django 5.0 on 2023-12-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('owner', models.IntegerField()),
                ('is_folder', models.BooleanField()),
                ('parent', models.IntegerField()),
                ('shared', models.BooleanField()),
                ('shared_with', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NUsers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
