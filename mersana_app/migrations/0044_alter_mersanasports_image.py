# Generated by Django 5.0.6 on 2024-06-13 19:18

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mersana_app', '0043_alter_mersanasports_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mersanasports',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[500, 300], upload_to='uploads/mersana_sports'),
        ),
    ]