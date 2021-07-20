from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class LandingView(TemplateView):
    template_name = "home/presentacion.html"

class EsperaView(TemplateView):
    template_name = "home/enconstruccion.html"

class HomeView(TemplateView):
    template_name = "home/home.html"
