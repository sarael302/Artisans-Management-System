from django import forms
from .models import Profile


class UpdateProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    expertise = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    hourly_rate = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    about_me = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


    class Meta:
        model = Profile
        fields = ['name', 'expertise', 'profile_image', 'about_me', 'hourly_rate', 'is_artisan', 'country', 'city']