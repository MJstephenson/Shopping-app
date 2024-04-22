from django.shortcuts import render, redirect
from .forms import SubscriberForm

def newsletter_signup(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsletter_confirmation')
    else:
        form = SubscriberForm()
    return render(request, 'home/index.html', {'form': form})

def newsletter_confirmation(request):
    return render(request, 'newsletter/newsletter_confirmation.html')