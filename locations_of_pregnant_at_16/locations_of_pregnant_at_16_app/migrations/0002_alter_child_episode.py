# Generated by Django 5.1.1 on 2024-10-03 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations_of_pregnant_at_16_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='locations_of_pregnant_at_16_app.episode', verbose_name='Эпизод'),
        ),
    ]
