from sweetify import sweetify
from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from mersana_app.forms import CommentForm
from mersana_app.models import Slider, Comment, LastNews, lastNewsGallery, Book, MersanaTrip, MersanaPiano, \
    MersanaPaints, MersanaSchool, MersanaFriends, MersanaMusic, MersanaSports, MersanaPic, ImportantTitle


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    model = LastNews

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['news'] = LastNews.objects.filter(is_active=True).order_by('-created_at')[:2]
        context['sliders'] = Slider.objects.filter(is_active=True)
        context['comments'] = Comment.objects.filter(is_active=True).order_by('-created_at')[:12]
        context['books'] = Book.objects.filter(is_active=True).order_by('-date')
        context['trips'] = MersanaTrip.objects.filter(is_active=True)
        context['pianos'] = MersanaPiano.objects.filter(is_active=True)
        context['paints'] = MersanaPaints.objects.filter(is_active=True)
        context['schools'] = MersanaSchool.objects.filter(is_active=True)
        context['friends'] = MersanaFriends.objects.filter(is_active=True)
        context['musics'] = MersanaMusic.objects.filter(is_active=True).order_by('-date')
        context['sports'] = MersanaSports.objects.filter(is_active=True)
        context['pictures'] = MersanaPic.objects.filter(is_active=True).order_by('-created_at')[:12]
        context['titles'] = ImportantTitle.objects.filter(is_active=True)

        return context


def show_images(request):
    images = MersanaPic.objects.all()
    context = {'images': images}
    return context

def news_detail(request: HttpRequest, id):
    new = lastNewsGallery.objects.get(id=id)
    context = {
        'new': new
    }
    return context


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


def site_header_component(request):
    return render(request, 'partials/header_component.html',{})


def site_footer_component(request):
    return render(request, 'partials/footer_component.html',{})