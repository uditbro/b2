from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
    #include default auth urls.
    path('',include('django.contrib.auth.urls')),
    # Registration page.
    path('register/',views.register, name='register'),
    #redirecticting from the login page.
    path('login/',views.login, name="login"),
]