# Generated by Django 5.0.6 on 2024-06-01 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mersana_app', '0009_lastnews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastnews',
            name='content',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
    ]
