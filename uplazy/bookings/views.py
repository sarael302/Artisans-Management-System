from django.shortcuts import render
from .models import Booking
from account.models import Profile
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def BookProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {
        'profile': profile,
        'success_message': '',
    }

    if request.method == 'POST':
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        date = request.POST.get('booking-date')
        book = Booking.objects.create(subject=subject, body=body, date=date, artisan=profile, booker=request.user.profile)
        context['success_message'] = ' '

    return render(request, 'book-form.html', context)



@login_required(login_url='login')
def Inbox(request):
    bookings = Booking.objects.filter(artisan=request.user.profile)

    context = {
        'bookings': bookings,
    }

    return render(request, 'inbox.html', context)


@login_required(login_url='login')
def BookingDetails(request, pk):
    BookingItem = Booking.objects.get(id=pk)
    BookingItem.is_read = True
    BookingItem.save()

    context = {
        'book': BookingItem,
        'success_message': ''
    }

    if request.method == 'POST' and (request.user.profile == BookingItem.artisan):
        BookingItem.is_confirmed = True
        BookingItem.save()
        context['success_message'] = 'd'


    return render(request, 'book.html', context)