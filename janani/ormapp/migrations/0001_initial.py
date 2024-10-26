# Generated by Django 5.1.2 on 2024-10-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Name', models.CharField(max_length=10)),
                ('accno', models.IntegerField(primary_key='accno', serialize=False)),
                ('phno', models.IntegerField()),
                ('income', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]