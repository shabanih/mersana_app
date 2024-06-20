# Generated by Django 5.0.6 on 2024-06-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mersana_app', '0008_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='')),
                ('content', models.TextField(verbose_name='')),
                ('image', models.ImageField(upload_to='uploads/lastnews', verbose_name='')),
                ('is_active', models.BooleanField(default=True, verbose_name='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='')),
            ],
        ),
    ]