from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models.signals import post_save
from shortuuid.django_fields import ShortUUIDField


class User(AbstractUser):
    full_name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(verbose_name='email address', unique=True)
    username = models.CharField(max_length=20, unique=True)
    mobile = models.CharField(max_length=11, verbose_name='تلفن همراه')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.full_name


class Profile(models.Model):
    pid = ShortUUIDField(primary_key=True, length=7, editable=False, max_length=25,
                         alphabet="abcdefghijklmnopqrstuvwxyz123", unique=True, verbose_name='')
    image = models.ImageField(upload_to='uploads/images/profile_image', null=True, blank=True, verbose_name='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='')
    mobile = models.CharField(max_length=11, verbose_name='تلفن همراه')
    full_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='')

    state = models.CharField(max_length=100, null=True, blank=True, verbose_name='')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='')
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='')
    postal_code = models.CharField(max_length=10, verbose_name='')

    date = models.DateTimeField(auto_now=True, verbose_name='')
    is_active = models.BooleanField(default=True, verbose_name='')

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        if self.full_name:
            return f'{self.full_name}'
        else:
            return f'{self.user.username}'

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    post_save.connect(create_user_profile, sender=User)
    post_save.connect(save_user_profile, sender=User)