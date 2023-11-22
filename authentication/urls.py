from xml.etree.ElementInclude import include
from django.urls import path
from authentication.views import login

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('auth/', include('authentication.urls')),
]