# Generated by Django 5.0 on 2023-12-20 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0007_remove_employee_compensations_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='about',
            field=models.CharField(default='default about', max_length=10000),
            preserve_default=False,
        ),
    ]
