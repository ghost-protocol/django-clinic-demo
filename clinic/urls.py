from django.urls import path
from .views import HomeTemplateView, ContactTemplateView, AboutTemplateView, ServicesTemplateView, AppointmentTemplateView


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about', AboutTemplateView.as_view(), name='about'),
    path('services', ServicesTemplateView.as_view(), name='services'),
    path('appointment', AppointmentTemplateView.as_view(), name='appointment'),
    path('contact', ContactTemplateView.as_view(), name='contact'),
]
