from django.urls import path, include
from app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('event/', event, name='event'),
    path('details/', details, name='details'),
    path('send/', send, name='send')

]
