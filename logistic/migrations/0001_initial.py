import django.db.models.deletion

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('registerDate', models.DateField()),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='logistic.user')),

            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerDate', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('executionDate', models.DateField()),
                ('place', models.CharField(max_length=200)),
                ('manager', models.CharField(max_length=200)),
                ('progress', models.IntegerField()),
                ('finishDate', models.DateField()),
            ],
        ),
    ]
