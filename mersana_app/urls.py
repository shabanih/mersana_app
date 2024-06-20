from django.urls import path

from mersana_app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('send-comment', views.comment, name='send_comment'),
    # path('image-gallery/<int:id>/', views.news_detail, name='image_gallery'),
    path('about-us', views.about_us, name='about_us'),
    path('conatct-us', views.contact_us, name='contact_us'),
]