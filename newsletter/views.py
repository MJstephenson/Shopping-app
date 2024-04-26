from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import SubscriberForm


def newsletter_signup(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # send the user a confirmation email
                email = request.POST.get("email")
                subject = "Subscription to Shopaholic"
                body = (
                    """
Thanks for subscribing to Shopaholic!
We offer a wide variety of beverages
for all kinds of tastes.
Be sure to check back often for clearance,
offers, sales, and more!

Cheers!
shopaholic@example.com
Shopaholic Team
                    """
                )
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [email]
                )
                return redirect('newsletter_confirmation')
            except IntegrityError:
                messages.error(
                    request, "This email address has already been subscribed."
                )
        else:
            messages.error(request, "Please check your input.")
    else:
        form = SubscriberForm()
    return render(request, 'home/index.html', {'form': form})


def newsletter_confirmation(request):
    return render(request, 'newsletter/newsletter_confirmation.html')
