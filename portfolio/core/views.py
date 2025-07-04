from django.shortcuts import render, redirect
from .models import PersonalInfo
from .forms import ContactForm

def home(request):
    info = PersonalInfo.objects.first()
    return render(request, 'home.html', {'info': info})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
