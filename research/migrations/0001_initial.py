# Generated by Django 3.2.9 on 2021-11-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='research_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10, unique=True)),
                ('period', models.CharField(blank=True, max_length=10)),
                ('range', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=20)),
                ('institute', models.CharField(max_length=20)),
                ('stage', models.CharField(max_length=20)),
                ('target_number', models.IntegerField()),
                ('office', models.CharField(max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'research_informations',
            },
        ),
    ]
