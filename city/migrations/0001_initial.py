# Generated by Django 4.0.3 on 2022-04-12 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Continent',
                'db_table': 'continents',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('updated', models.DateField(auto_now=True, verbose_name='Time updated')),
                ('is_published', models.BooleanField(default=True)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='city.continent')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'cities',
                'ordering': ['-created'],
            },
        ),
    ]
