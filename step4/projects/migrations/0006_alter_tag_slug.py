# Generated by Django 4.0.6 on 2022-07-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100)),
        ),
    ]
