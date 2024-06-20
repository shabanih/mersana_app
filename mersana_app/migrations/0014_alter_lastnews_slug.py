# Generated by Django 5.0.6 on 2024-06-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mersana_app', '0013_alter_lastnews_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastnews',
            name='slug',
            field=models.SlugField(default='', max_length=200, null=True, unique=True, verbose_name='عنوان در url'),
        ),
    ]