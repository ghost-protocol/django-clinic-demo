import datetime

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage

from django.views.generic.base import TemplateView



class HomeTemplateView(TemplateView):
    template_name = "index.html"

class AboutTemplateView(TemplateView):
    template_name = "about.html"

class ServicesTemplateView(TemplateView):
    template_name = "services.html"
    

class ContactTemplateView(TemplateView):
    template_name = "contact.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # email = EmailMessage(
        #     subject= f"{name} from doctor family.",
        #     body=message,
        #     from_email=settings.EMAIL_HOST_USER,
        #     to=[settings.EMAIL_HOST_USER],
        #     reply_to=[email]
        # )
        # email.send()

        messages.add_message(request, messages.SUCCESS, f"Thanks {name} for contacting us. Our agents will respond to you ASAP")
        return HttpResponseRedirect(request.path)
        # messages.success(request, 'Email submitted successfully!')
        # return HttpResponse("Email sent successfully!")
        # return redirect(request.META.get('HTTP_REFERER', '/'))  # Redirect to the previous page or '/' if not available


class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        doctor = request.POST.get("doctor")
        date = request.POST.get("date")
        time = request.POST.get("time")
        problem = request.POST.get("problem")

        # email = EmailMessage(
        #     subject= f"{name} from doctor family.",
        #     body=message,
        #     from_email=settings.EMAIL_HOST_USER,
        #     to=[settings.EMAIL_HOST_USER],
        #     reply_to=[email]
        # )
        # email.send()

        print(name, email, mobile, doctor, date+time, problem)

        messages.add_message(request, messages.SUCCESS, f"Thanks {name} for booking an appointment for {date, time}. Our agents will respond to you ASAP")
        return HttpResponseRedirect(request.path)