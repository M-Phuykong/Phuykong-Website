from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'personalweb/home.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        # NEED TO ADD ELSE FOR WHEN THE FORM FAILS
        if form.is_valid():
            form.save()
            email_subject = f'{form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
            # NEED TO CHANGE THIS TO A SUCCESS MESSAGE AFTERING SENDING THE EMAIL
            return render(request, 'personalweb/about.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'personalweb/contact.html', context)

def about(request):
    return render(request, 'personalweb/about.html')
    