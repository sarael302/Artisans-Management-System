from django.urls import path
from .views import AccountLogin, AccountSignup, AccountLogout, AccountProfile, AccountSettings, FilterAccounts


urlpatterns = [
    path('login/', AccountLogin, name='login'),
    path('signup/', AccountSignup, name='signup'),
    path('logout/', AccountLogout, name='logout'),
    path('profile/<str:pk>/', AccountProfile, name='profile'),
    path('settings/', AccountSettings, name='settings'),
    path('filter/', FilterAccounts, name='filter'),

]

