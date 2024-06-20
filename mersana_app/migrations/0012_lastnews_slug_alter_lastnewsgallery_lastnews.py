# Generated by Django 5.0.6 on 2024-06-04 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mersana_app', '0011_alter_lastnews_content_alter_lastnews_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastnews',
            name='slug',
            field=models.SlugField(default='', max_length=200, null=True, unique=True, verbose_name='عنوان در url'),
        ),
        migrations.AlterField(
            model_name='lastnewsgallery',
            name='lastnews',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mersana_app.lastnews', verbose_name='آخرین خبر'),
        ),
    ]