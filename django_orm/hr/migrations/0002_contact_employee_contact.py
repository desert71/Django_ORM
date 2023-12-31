# Generated by Django 5.0 on 2023-12-13 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='contact',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.contact'),
        ),
    ]
