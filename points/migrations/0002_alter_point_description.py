# Generated by Django 4.1.7 on 2023-03-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
