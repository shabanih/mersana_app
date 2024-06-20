from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from mersana_app.forms import CommentForm, ContactForm
from mersana_app.models import Slider, Comment, LastNews, lastNewsGallery, Book, MersanaTrip, MersanaPiano, \
    MersanaPaints, MersanaSchool, MersanaFriends, MersanaMusic, MersanaSports, MersanaPic, SectionTitle, \
    SectionTitlePage, ContactUs, ContactInfo, VisitCount, AboutUs


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    model = LastNews

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        visit_count, created = VisitCount.objects.get_or_create(id=1)
        visit_count.count += 1
        visit_count.save()

        context['visit_count'] = visit_count.count
        context['news'] = LastNews.objects.filter(is_active=True).order_by('-created_at')[:2]
        context['sliders'] = Slider.objects.filter(is_active=True).order_by('-created_at')
        context['comments'] = Comment.objects.filter(is_active=True).order_by('-created_at')[:12]
        context['books'] = Book.objects.filter(is_active=True).order_by('-created_at')
        context['trips'] = MersanaTrip.objects.filter(is_active=True)
        context['pianos'] = MersanaPiano.objects.filter(is_active=True).order_by('-date')
        context['paints'] = MersanaPaints.objects.filter(is_active=True).order_by('-date')[:7]
        context['schools'] = MersanaSchool.objects.filter(is_active=True)
        context['friends'] = MersanaFriends.objects.filter(is_active=True).order_by('-create_at')
        context['musics'] = MersanaMusic.objects.filter(is_active=True).order_by('-date')
        context['sports'] = MersanaSports.objects.filter(is_active=True).order_by('-created_at')
        context['pictures'] = MersanaPic.objects.filter(is_active=True).order_by('-created_at')[:12]
        context['titles'] = SectionTitle.objects.filter(is_active=True)
        context['sectionTitles'] = SectionTitlePage.objects.filter(is_active=True).select_related('section_title')
        context['contacts'] = ContactInfo.objects.filter(is_active=True)

        return context


def show_images(request):
    images = MersanaPic.objects.all()
    context = {'images': images}
    return context


# def news_detail(request: HttpRequest, pk):
#     new = lastNewsGallery.objects.get(id=pk)
#     context = {
#         'new': new
#     }
#     return context


def comment(request: HttpRequest):
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect(reverse('index'))
        else:
            messages.error(request, 'لطفا موارد ذیل را بررسی کنید.')

    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def about_us(request: HttpRequest):
    abouts = AboutUs.objects.filter(is_active=True).order_by('-created_at')[:1]
    return render(request, 'about_us.html', {'abouts': abouts})


def book_more_info(request: HttpRequest):
    books = Book.objects.all()
    return render(request, 'book_more_info.html', {'books': books})


def contact_us(request: HttpRequest):
    contacts = ContactInfo.objects.filter(is_active=True)
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        mobile = request.POST['mobile']
        message = request.POST['message']

        if form.is_valid():
            comments = ContactUs.objects.create(name=name, subject=subject, message=message, mobile=mobile)
            comments.save()
            messages.success(request, 'پیام شما با موفقیت ارسال گردید. پس از بررسی در صورت ثبت شماره تماس و یا ایمیل با شما ارتباط  خواهم گرفت.')
            return redirect(reverse('contact_us'))
        else:
            messages.error(request, 'لطفا موارد ذیل را بررسی کنید.')

    context = {
        'form': form,
        'contacts': contacts
    }
    return render(request, 'contact_us.html', context)


def site_header_component(request):
    return render(request, 'partials/header_component.html', {})


def site_footer_component(request):
    return render(request, 'partials/footer_component.html', {})
