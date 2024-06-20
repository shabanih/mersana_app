# Generated by Django 5.0.6 on 2024-06-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mersana_app', '0021_alter_mersanapaints_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mersanaschool',
            name='date',
            field=models.CharField(max_length=100, verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='mersanaschool',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='mersanaschool',
            name='image',
            field=models.FileField(upload_to='uploads/mersana_school', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='mersanaschool',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال/غیرفعال'),
        ),
        migrations.AlterField(
            model_name='mersanaschool',
            name='period',
            field=models.CharField(max_length=200, verbose_name='دوره'),
        ),
        migrations.AlterField(
            model_name='mersanaschool',
            name='school_address',
            field=models.CharField(max_length=200, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='mersanaschool',
            name='school_name',
            field=models.CharField(max_length=200, verbose_name='نام مدرسه'),
        ),
        migrations.AlterField(
            model_name='mersanaschool',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='عنوان در url'),
        ),
        migrations.AlterField(
            model_name='mersanaschool',
            name='teacher_name',
            field=models.CharField(max_length=200, verbose_name='نام معلم'),
        ),
    ]