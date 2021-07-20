from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_ciudadano = models.BooleanField(default=False)
    is_organizacion = models.BooleanField(default=False)
    is_convencional = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')



class Ciudadano(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    email = models.EmailField(max_length=255)
    cualquiercosa = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Ciudadan@"
        verbose_name_plural = "Ciudadan@s"

    def __str__(self):
        return self.user.username



class Organizacion(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    email = models.EmailField(max_length=255)
    cualquiercosa = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Organzación"
        verbose_name_plural = "Organizaciones"

    def __str__(self):
        return self.user.username



class Convencional(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    email = models.EmailField(max_length=255)
    cualquiercosa = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Convencional"
        verbose_name_plural = "Convencionales"

    def __str__(self):
        return self.user.username
