from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, ContactMessage
from .forms import ContactForm


def home(request):
    """Render the home page with featured services."""
    services = Service.objects.filter(is_active=True)[:6]
    context = {
        'services': services,
    }
    return render(request, 'main/home.html', context)


def about(request):
    """Render the about us page."""
    return render(request, 'main/about.html')


def services(request):
    """Render the services page with all active services."""
    services = Service.objects.filter(is_active=True)
    context = {
        'services': services,
    }
    return render(request, 'main/services.html', context)


def contact(request):
    """Render the contact us page and handle form submissions."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! We will get back to you within 24 hours.')
            return redirect('main:contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'main/contact.html', context)
