from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', LandingView.as_view()),
    path('enconstruccion/', EsperaView.as_view()),
    path('home/', HomeView.as_view(), name='home'),
]
