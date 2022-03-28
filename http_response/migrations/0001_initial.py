# Generated by Django 4.0.3 on 2022-03-27 16:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HttpResponseMimicker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('status_code', models.IntegerField(default=200, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(599)])),
                ('json_response', models.JSONField()),
            ],
        ),
    ]
