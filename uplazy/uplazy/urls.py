
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from account.models import Profile
from django.db.models import Q


def home(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.all().filter(is_artisan=True).exclude(id=request.user.profile.id)
    else:
        profiles = Profile.objects.all().filter(is_artisan=True)

    if request.method == 'POST':
        search_q = request.POST.get('query')
  
        if search_q:
            profiles = profiles.filter(expertise__icontains=search_q)





    context = {
        'profiles': profiles,
        'profiles_count': len(profiles),
    }


    return render(request, 'home.html', context)


def faqs(request):
    return render(request, 'faqs.html')



urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('booking/', include('bookings.urls')),
    path('faqs/', faqs, name='faqs')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)