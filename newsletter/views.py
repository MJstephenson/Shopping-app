from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from .forms import SubscriberForm

def newsletter_signup(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('newsletter_confirmation')
            except IntegrityError:
                messages.error(request, "This email address has already been subscribed.")
        else:
            messages.error(request, "Please check your input.")
    else:
        form = SubscriberForm()
    return render(request, 'home/index.html', {'form': form})

def newsletter_confirmation(request):
    return render(request, 'newsletter/newsletter_confirmation.html')
