import os

import PIL
from PIL import Image as PilImage
from django.core.files.storage import default_storage
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_cleanup import cleanup
from django_resized import ResizedImageField


class SectionTitle(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True, verbose_name="عنوان")
    created_at = models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    def section_title(self):
        return lastNewsGallery.objects.filter(section_title=self)


class SectionTitlePage(models.Model):
    section_title = models.ForeignKey(SectionTitle, on_delete=models.CASCADE, null=True, blank=True,
                                      verbose_name="", related_name="section_title_page")
    title_page = models.CharField(max_length=300, null=True, blank=True, verbose_name=" پیام")
    created_at = models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.section_title.title


@cleanup.select
class MersanaPic(models.Model):
    name = models.CharField(max_length=20, verbose_name='نام')
    image = ResizedImageField(upload_to='uploads/mersana_pictures', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')
    created_at = models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                # Get the existing instance from the database
                old_instance = MersanaPic.objects.get(pk=self.pk)
                # Check if the image field has changed
                if old_instance.image and old_instance.image != self.image:
                    # If so, delete the old image file
                    old_instance.image.delete(save=False)
            except MersanaPic.DoesNotExist:
                # Handle the case where the instance does not exist
                pass
        # Save the new image
        super(MersanaPic, self).save(*args, **kwargs)


@cleanup.select
class MersanaFriends(models.Model):
    name = models.CharField(max_length=20, verbose_name='نام')
    important_title = models.CharField(max_length=300, verbose_name='تیتر بالا')
    image = ResizedImageField(upload_to='uploads/mersana_friends', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    create_at = models.DateField(auto_now_add=True, verbose_name='تاریخ')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                # Get the existing instance from the database
                old_instance = MersanaFriends.objects.get(pk=self.pk)
                # Check if the image field has changed
                if old_instance.image and old_instance.image != self.image:
                    # If so, delete the old image file
                    old_instance.image.delete(save=False)
            except MersanaFriends.DoesNotExist:
                # Handle the case where the instance does not exist
                pass
        # Save the new image
        super(MersanaFriends, self).save(*args, **kwargs)


@cleanup.select
class MersanaPaints(models.Model):
    title = models.CharField(max_length=500, verbose_name='عنوان')
    image = ResizedImageField(upload_to='uploads/mersana_paints', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')
    date = models.DateField(verbose_name='تاریخ')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                # Get the existing instance from the database
                old_instance = MersanaPaints.objects.get(pk=self.pk)
                # Check if the image field has changed
                if old_instance.image and old_instance.image != self.image:
                    # If so, delete the old image file
                    old_instance.image.delete(save=False)
            except MersanaPaints.DoesNotExist:
                # Handle the case where the instance does not exist
                pass
        # Save the new image
        super(MersanaPaints, self).save(*args, **kwargs)


@cleanup.select
class MersanaPiano(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    video = models.FileField(upload_to='uploads/mersana_piano', verbose_name='ویدیو')
    description = models.TextField(verbose_name='توضیحات')
    date = models.DateField(verbose_name='زمان')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                # Get the existing instance from the database
                old_instance = MersanaPiano.objects.get(pk=self.pk)
                # Check if the image field has changed
                if old_instance.video and old_instance.video != self.video:
                    # If so, delete the old image file
                    old_instance.video.delete(save=False)
            except MersanaPiano.DoesNotExist:
                # Handle the case where the instance does not exist
                pass
        # Save the new image
        super(MersanaPiano, self).save(*args, **kwargs)


@cleanup.select
class MersanaMusic(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    music = models.FileField(upload_to='uploads/mersana_music', verbose_name='موسیقی')
    description = models.TextField(verbose_name='توضیحات')
    date = models.DateField(verbose_name='تاریخ')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                # Get the existing instance from the database
                old_instance = MersanaMusic.objects.get(pk=self.pk)
                # Check if the image field has changed
                if old_instance.music and old_instance.music != self.music:
                    # If so, delete the old image file
                    old_instance.music.delete(save=False)
            except MersanaMusic.DoesNotExist:
                # Handle the case where the instance does not exist
                pass
        # Save the new image
        super(MersanaMusic, self).save(*args, **kwargs)


@cleanup.select
class MersanaCreativity(models.Model):
    title = models.CharField(max_length=200, verbose_name='')
    image = ResizedImageField(upload_to='uploads/mersana_creativity', verbose_name='')
    description = models.TextField(verbose_name='')
    date = models.DateField(verbose_name='')
    slug = models.SlugField(max_length=200, verbose_name='')
    is_active = models.BooleanField(default=True, verbose_name='')

    def __str__(self):
        return self.title


@cleanup.select
class MersanaSchool(models.Model):
    school_name = models.CharField(max_length=200, verbose_name='نام مدرسه')
    school_address = models.CharField(max_length=200, verbose_name='آدرس')
    teacher_name = models.CharField(max_length=200, verbose_name='نام معلم')
    image = ResizedImageField(upload_to='uploads/mersana_school', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')
    period = models.CharField(max_length=200, verbose_name='دوره')
    date = models.CharField(max_length=100, verbose_name='تاریخ')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.school_name

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                # Get the existing instance from the database
                old_instance = MersanaSchool.objects.get(pk=self.pk)
                # Check if the image field has changed
                if old_instance.image and old_instance.image != self.image:
                    # If so, delete the old image file
                    old_instance.image.delete(save=False)
            except MersanaSchool.DoesNotExist:
                # Handle the case where the instance does not exist
                pass
        # Save the new image
        super(MersanaSchool, self).save(*args, **kwargs)


@cleanup.select
class MersanaTrip(models.Model):
    trip_title = models.CharField(max_length=200, verbose_name='عنوان سفر')
    trip_date = models.CharField(max_length=100, verbose_name='زمان سفر')
    city = models.CharField(max_length=200, verbose_name='شهر')
    image = ResizedImageField(upload_to='uploads/mersana_trip', verbose_name='تصویر')
    trip_description = models.TextField(verbose_name='شرح سفر')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.trip_title

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                # Get the existing instance from the database
                old_instance = MersanaTrip.objects.get(pk=self.pk)
                # Check if the image field has changed
                if old_instance.image and old_instance.image != self.image:
                    # If so, delete the old image file
                    old_instance.image.delete(save=False)
            except MersanaTrip.DoesNotExist:
                # Handle the case where the instance does not exist
                pass
        # Save the new image
        super(MersanaTrip, self).save(*args, **kwargs)


@cleanup.select
class MersanaSports(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام')
    description = models.TextField(verbose_name='توضیحات')
    # image = models.ImageField(upload_to='mersana_sports', verbose_name='تصویر')
    image = ResizedImageField(upload_to='uploads/mersana_sports')
    date = models.DateField(verbose_name='تاریخ')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if self.pk:
            try:
                # Get the existing instance from the database
                old_instance = MersanaSports.objects.get(pk=self.pk)
                # Check if the image field has changed
                if old_instance.image and old_instance.image != self.image:
                    # If so, delete the old image file
                    old_instance.image.delete(save=False)
            except MersanaSports.DoesNotExist:
                # Handle the case where the instance does not exist
                pass
        # Save the new image
        super(MersanaSports, self).save(*args, **kwargs)


@cleanup.select
class Book(models.Model):
    title_book = models.CharField(max_length=200, verbose_name='عنوان کتاب')
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی')
    music_book = models.URLField(null=True, verbose_name='لینک صدای داستان')
    image = ResizedImageField(upload_to='uploads/books', verbose_name='تصویر اصلی', null=True, blank=True)

    author = models.CharField(max_length=200, verbose_name='نویسنده')
    publisher = models.CharField(max_length=200, verbose_name='ناشر')
    translator = models.CharField(max_length=200, verbose_name='مترجم', null=True, blank=True)
    page_counts = models.CharField(max_length=200, verbose_name='تعداد صفحات')
    year_of_publication = models.CharField(max_length=50, verbose_name='سال انتشار')

    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')

    def __str__(self):
        return self.title_book

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                # Get the existing instance from the database
                old_instance = Book.objects.get(pk=self.pk)
                # Check if the image field has changed
                if old_instance.image and old_instance.image != self.image:
                    # If so, delete the old image file
                    old_instance.image.delete(save=False)
            except Book.DoesNotExist:
                # Handle the case where the instance does not exist
                pass
        # Save the new image
        super(Book, self).save(*args, **kwargs)


@cleanup.select
class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    image = models.ImageField(upload_to='uploads/slider', verbose_name='تصویر')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')
    is_deleted = models.BooleanField(default=False, verbose_name='حذف شده/ نشده')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return str(self.image)

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                # Get the existing instance from the database
                old_instance = Slider.objects.get(pk=self.pk)
                # Check if the image field has changed
                if old_instance.image and old_instance.image != self.image:
                    # If so, delete the old image file
                    old_instance.image.delete(save=False)
            except Slider.DoesNotExist:
                # Handle the case where the instance does not exist
                pass
        # Save the new image
        super(Slider, self).save(*args, **kwargs)


class Comment(models.Model):
    name = models.CharField(max_length=200, verbose_name='')
    message = models.TextField(verbose_name='')
    is_active = models.BooleanField(default=True, verbose_name='')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='')

    def __str__(self):
        return self.name


class LastNews(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    content = models.CharField(max_length=100, verbose_name='توضیحات')
    slug = models.SlugField(db_index=True, default='', null=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.title

    def news_gallery(self):
        return lastNewsGallery.objects.filter(lastnews=self)


@cleanup.select
class lastNewsGallery(models.Model):
    lastnews = models.ForeignKey(LastNews, on_delete=models.CASCADE, related_name="news_gallery", verbose_name='آخرین خبر')
    image = ResizedImageField(upload_to='uploads/lastnewsGallery', verbose_name='تصویر')
    is_active = models.BooleanField(default=True, verbose_name='')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='')

    def __str__(self):
        return self.lastnews.title

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                # Get the existing instance from the database
                old_instance = lastNewsGallery.objects.get(pk=self.pk)
                # Check if the image field has changed
                if old_instance.image and old_instance.image != self.image:
                    # If so, delete the old image file
                    old_instance.image.delete(save=False)
            except Slider.DoesNotExist:
                # Handle the case where the instance does not exist
                pass
        # Save the new image
        super(lastNewsGallery, self).save(*args, **kwargs)


@cleanup.select
class AboutUs(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = ResizedImageField(upload_to='uploads/aboutUs', verbose_name='تصویر', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=200, verbose_name='')
    subject = models.CharField(max_length=200, verbose_name='')
    message = models.TextField(max_length=360, verbose_name="پیام")
    mobile = models.CharField(max_length=100, null=False, blank=False, verbose_name="")
    is_active = models.BooleanField(default=True, verbose_name='')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='')

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    address = models.CharField(max_length=200, verbose_name='ادرس')
    phone = models.CharField(max_length=200, verbose_name='شماره تلفن')
    email = models.CharField(max_length=200, verbose_name='آدرس ایمیل')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ثبت')

    def __str__(self):
        return self.phone


class VisitCount(models.Model):
    count = models.PositiveIntegerField(default=0)
