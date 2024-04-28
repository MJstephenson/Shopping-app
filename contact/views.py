from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
                form.instance.email = user.email
            form.save()
            return redirect('thank_you')
    else:
        if request.user.is_authenticated:
            user = request.user
            initial_data = {
                'email': user.email,
            }
            form = ContactForm(initial=initial_data)
        else:
            form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/contact.html', context)


def thank_you_view(request):
    return render(request, 'contact/thank_you.html')
