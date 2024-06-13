from django.db import models


# Create your models here.

class ImportantTitle(models.Model):
    title_of_friends = models.CharField(max_length=300, null=True, blank=True, verbose_name="Title Of Friends")
    created_at = models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')


class MersanaPic(models.Model):
    name = models.CharField(max_length=20, verbose_name='نام')
    image = models.ImageField(upload_to='uploads/mersana_pictures', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')
    created_at = models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.name


class MersanaFriends(models.Model):
    name = models.CharField(max_length=20, verbose_name='نام')
    important_title = models.CharField(max_length=300, verbose_name='تیتر بالا')
    image = models.ImageField(upload_to='uploads/mersana_friends', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    create_at = models.DateField(auto_now_add=True, verbose_name='تاریخ')

    def __str__(self):
        return self.name


class MersanaPaints(models.Model):
    title = models.CharField(max_length=500, verbose_name='عنوان')
    image = models.ImageField(upload_to='uploads/mersana_paints', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')
    date = models.DateField(verbose_name='تاریخ')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title


class MersanaPiano(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    video = models.FileField(upload_to='uploads/mersana_piano', verbose_name='ویدیو')
    description = models.TextField(verbose_name='توضیحات')
    date = models.DateField(verbose_name='زمان')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title


class MersanaMusic(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    music = models.FileField(upload_to='uploads/mersana_music', verbose_name='موسیقی')
    description = models.TextField(verbose_name='توضیحات')
    date = models.DateField(verbose_name='تاریخ')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title


class MersanaCreativity(models.Model):
    title = models.CharField(max_length=200, verbose_name='')
    image = models.ImageField(upload_to='uploads/mersana_creativity', verbose_name='')
    description = models.TextField(verbose_name='')
    date = models.DateField(verbose_name='')
    slug = models.SlugField(max_length=200, verbose_name='')
    is_active = models.BooleanField(default=True, verbose_name='')

    def __str__(self):
        return self.title


class MersanaSchool(models.Model):
    school_name = models.CharField(max_length=200, verbose_name='نام مدرسه')
    school_address = models.CharField(max_length=200, verbose_name='آدرس')
    teacher_name = models.CharField(max_length=200, verbose_name='نام معلم')
    image = models.FileField(upload_to='uploads/mersana_school', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')
    period = models.CharField(max_length=200, verbose_name='دوره')
    date = models.CharField(max_length=100, verbose_name='تاریخ')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.school_name


class MersanaTrip(models.Model):
    trip_title = models.CharField(max_length=200, verbose_name='عنوان سفر')
    trip_date = models.CharField(max_length=100, verbose_name='زمان سفر')
    city = models.CharField(max_length=200, verbose_name='شهر')
    image = models.FileField(upload_to='uploads/mersana_trip', verbose_name='تصویر')
    trip_description = models.TextField(verbose_name='شرح سفر')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.trip_title


class MersanaSports(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام')
    description = models.TextField(verbose_name='توضیحات')
    image = models.FileField(upload_to='uploads/mersana_sports', verbose_name='تصویر')
    date = models.DateField(verbose_name='تاریخ')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title


class Book(models.Model):
    title_book = models.CharField(max_length=200, verbose_name='عنوان کتاب')
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی')
    music_book = models.URLField(null=True, verbose_name='لینک صدای داستان')
    image_1 = models.ImageField(upload_to='uploads/books', verbose_name='تصویر اصلی', null=True, blank=True)
    pic = models.ImageField(upload_to='uploads/books', verbose_name='تصویر دوم', null=True, blank=True)
    date = models.DateField(verbose_name='تاریخ')
    slug = models.SlugField(max_length=200, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')

    def __str__(self):
        return self.title_book


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    image = models.ImageField(upload_to='uploads/slider', verbose_name='تصویر')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')
    is_deleted = models.BooleanField(default=False, verbose_name='حذف شده/ نشده')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return str(self.image)


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


class lastNewsGallery(models.Model):
    lastnews = models.ForeignKey(LastNews, on_delete=models.CASCADE, related_name="news_gallery", verbose_name='آخرین خبر')
    image = models.ImageField(upload_to='uploads/lastnewsGallery', verbose_name='تصویر')
    is_active = models.BooleanField(default=True, verbose_name='')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='')

    def __str__(self):
        return self.lastnews.title




