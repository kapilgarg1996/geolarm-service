# Generated by Django 2.2.3 on 2019-07-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('day', models.CharField(max_length=16)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('is_holiday', models.BooleanField()),
                ('is_special_day', models.BooleanField()),
            ],
            options={
                'db_table': 'logs',
            },
        ),
    ]
