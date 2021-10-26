from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()

        data = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message
        }
        message = '''
        Subject: {}
        Message: {}

        From: {}
        Name: {}
        '''.format(data['subject'],data['message'],data['email'],data['name'])

        send_mail(subject, message ,settings.EMAIL_HOST_USER,['niaz.caan@motiiv.co.uk'],fail_silently=False)

        return HttpResponse("Thanks for contacting us! We will do our best to get back to you as soon as we can.")
    return render(request, 'base/index.html')
