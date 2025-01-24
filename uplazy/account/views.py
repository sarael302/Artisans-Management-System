from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Review
from .forms import UpdateProfileForm
from bookings.models import Booking
from django.db.models import Q

def name_shortner(firstname: str, lastname: str):
    output = firstname.capitalize()[0] + '.' + lastname.upper()
    return output

def AccountLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    context = {
        'error_message':''
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context['error_message'] = 'email/password incorrect'

    return render(request, 'login.html', context)

def AccountSignup(request):
    if request.user.is_authenticated:
        return redirect('home')

    context = {
        'error_message': ''
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        country = request.POST.get('country')
        city = request.POST.get('city')
        is_artisan = request.POST.get('is_artisan')
        print(is_artisan)

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print(username)
                context['error_message'] = 'username already taken'
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=firstname, last_name=lastname)
                user.save()
                profile = Profile.objects.get(user=user)
                profile.name = name_shortner(firstname=firstname, lastname=lastname)
                profile.country = country
                profile.city = city
                profile.save()
                login(request, user)
                return redirect('home')
        else:
            context['error_message'] = 'incorrect confirmation password, try again'

    return render(request, 'sign-up.html', context)

def AccountLogout(request):
    logout(request)
    return redirect('home')

def AccountProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    able_to_comment = False
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(booker=request.user.profile, artisan=profile)
        if bookings:
            for booking in bookings:
                if booking.is_confirmed:
                    able_to_comment = True

        if len(Review.objects.filter(artisan=profile, reviewer=request.user.profile)) < 1:
            able_to_comment = True
        else:
            able_to_comment = False

    reviews = Review.objects.filter(artisan=profile)
    context = {
        'profile': profile,
        'error_message': '',
        'success_message': '',
        'reviews': reviews,
        'can_review': able_to_comment,
    }

    if request.method == 'POST':
        if request.user.is_authenticated:
            review = request.POST.get('review')
            new_review = Review.objects.create(reviewer=request.user.profile, artisan=profile, content=review)
            new_review.save()
        else:
            context['error_message'] = 'You need to be logged in to post a review.'

    return render(request, 'profile.html', context)

def AccountSettings(request):
    if not request.user.is_authenticated:
        return redirect('login')

    profile = Profile.objects.get(id=request.user.profile.id)

    context = {
        'profile_form': UpdateProfileForm(instance=request.user.profile),
        'profile': profile,
        'success_message': '',
        'error_message': '',
    }

    if request.method == 'POST':
        try:
            profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                context['success_message'] = 'Profile updated successfully!'
                return render(request, 'settings.html', context)
        except:
            context['error_message'] = 'Something went wrong!'

    return render(request, 'settings.html', context)

def FilterAccounts(request):
    context = {
        "profiles": [],
    }

    if request.method == 'POST':
        country = request.POST.get('country')
        city = request.POST.get('city')

        profiles = Profile.objects.filter(country__icontains=country, city__icontains=city)
        print(profiles)
        context['profiles'] = profiles
        return render(request, 'home.html', context)
    
    else:
        return redirect('home')
