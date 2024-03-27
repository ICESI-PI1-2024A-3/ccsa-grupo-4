# Generated by Django 5.0.3 on 2024-03-17 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0004_remove_event_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='logistic.event')),
            ],
        ),
    ]