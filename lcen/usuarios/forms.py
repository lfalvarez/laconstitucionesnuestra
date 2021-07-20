from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Ciudadano, Organizacion, Convencional


class CiudadanoSignUpForm(UserCreationForm):
    nombre = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    cualquiercosa = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_ciudadano = True
        user.nombre = self.cleaned_data.get('nombre')
        # user.last_name = self.cleaned_data.get('last_name')
        user.save()
        ciudadano = Ciudadano.objects.create(user=user)
        ciudadano.email=self.cleaned_data.get('email')
        ciudadano.cualquiercosa=self.cleaned_data.get('cualquiercosa')
        ciudadano.save()
        return user


class OrganizacionSignUpForm(UserCreationForm):
    nombre = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    cualquiercosa = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_organizacion = True
        user.nombre = self.cleaned_data.get('nombre')
        # user.last_name = self.cleaned_data.get('last_name')
        user.save()
        organizacion = Organizacion.objects.create(user=user)
        organizacion.email=self.cleaned_data.get('email')
        organizacion.cualquiercosa=self.cleaned_data.get('cualquiercosa')
        organizacion.save()
        return user


class ConvencionalSignUpForm(UserCreationForm):
    nombre = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    cualquiercosa = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_convencional = True
        user.nombre = self.cleaned_data.get('nombre')
        # user.last_name = self.cleaned_data.get('last_name')
        user.save()
        convencional = Convencional.objects.create(user=user)
        convencional.email=self.cleaned_data.get('email')
        convencional.cualquiercosa=self.cleaned_data.get('cualquiercosa')
        convencional.save()
        return user
