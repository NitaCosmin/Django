from django.shortcuts import render, redirect
from .models import PersonalInfo,User
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from .forms import PersonalInfoForm
from .forms import RegisterForm
from django.contrib.auth import login

@login_required
def profiles_list(request):
    profiles = PersonalInfo.objects.all()  # get all profiles
    return render(request, 'main/profiles_list.html', {'profiles': profiles})
@login_required
def profile_detail(request, user_id):
    profile = PersonalInfo.objects.get(user__id=user_id)
    return render(request, 'main/profile_detail.html', {'profile': profile})

def home(request, user_id=None):
 
    if not user_id and request.user.is_authenticated:
        user_id = request.user.id
    

    users_with_profiles = User.objects.filter(personalinfo__isnull=False).order_by('id')

    current_profile = None
    if user_id:
        try:
            current_profile = PersonalInfo.objects.get(user_id=user_id)
        except PersonalInfo.DoesNotExist:
            pass
   
    prev_user = next_user = None
    if user_id and users_with_profiles.exists():
        user_ids = list(users_with_profiles.values_list('id', flat=True))
        current_index = user_ids.index(int(user_id)) if int(user_id) in user_ids else -1
        
        if current_index > 0:
            prev_user = user_ids[current_index - 1]
        if current_index < len(user_ids) - 1:
            next_user = user_ids[current_index + 1]
    
    context = {
        'info': current_profile,
        'prev_user_id': prev_user,
        'next_user_id': next_user,
    }
    return render(request, 'home.html', context)
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})




@login_required
def edit_profile(request):
    personal_info, created = PersonalInfo.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, request.FILES, instance=personal_info)
        if form.is_valid():
            form.save()
            return redirect('home')  # sau unde vrei după salvare
    else:
        form = PersonalInfoForm(instance=personal_info)

    return render(request, 'edit_profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})