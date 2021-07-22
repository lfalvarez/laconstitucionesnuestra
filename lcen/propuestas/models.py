from django.db import models
from usuarios.models import User
from managers.models import Comuna
from convencionales.models import Constituyente



class TemaPropuesta(models.Model):
    tema_propuesta = models.CharField("Tema de Propuesta",
        max_length=100,
        unique=True,
        help_text="Temas predefinidos de propuestas")
    class Meta:
        verbose_name = "Tema Propuestas"
        verbose_name_plural = "Temas Propuestas"
    def __str__(self):
        return self.tema_propuesta



class ComponenteConstitucion(models.Model):
    componente_constitucion = models.CharField("Componente Constitucional",
        max_length=100,
        unique=True,
        help_text="Componente Constitucional de Propuesta")
    class Meta:
        verbose_name = "Componente Constitucional"
        verbose_name_plural = "Componentes Constitucionales"
    def __str__(self):
        return self.componente_constitucion



class Propuesta(models.Model):
    autor = models.ForeignKey(User,
        verbose_name="Autor@ de Propuesta",
        null=True,
        on_delete=models.SET_NULL)
    tema = models.ForeignKey(TemaPropuesta,
        null=True,
        help_text="¿Cuál es el tema principal de tu propuesta? Por favor selecciona una categoría del siguiente listado, pues nos ayudará a organizar temáticamente las propuestas en el buscador de la plataforma.",
        on_delete=models.SET_NULL)
    otros_temas = models.ManyToManyField(TemaPropuesta,
        related_name="otros_temas_propuesta",
        verbose_name="Otros Temas de Propuesta",
        help_text="¿Qué otros temas aborda tu propuesta? Por favor selecciona hasta tres temas adicionales.")
    problema = models.TextField("Descripción de problema a solucionar",
        max_length=225,
        null=True,
        blank=True,
        help_text="¿Cuál es el problema que tú o tu organización busca solucionar?")
    situacion = models.TextField("Situación ideal de solución",
        null=True,
        blank=True,
        help_text="Con respecto al problema planteado, ¿cuál sería la situación ideal?")
    componente = models.TextField("Componente de la Constitución",
        null=True,
        blank=True,
        help_text="Para avanzar en el logro de esa situación ideal, ¿qué debería contemplar la Nueva Constitución?")
    otras_organizaciones = models.BooleanField("Junto a otras organizaciones",
        default=False,
        help_text="¿Esta propuesta fue elaborada en conjunto con otras organizaciones?")
    organizaciones_de_propuesta = models.TextField("Otras Organizaciones",
        null=True,
        blank=True,
        help_text="Si tu respuesta fue 'sí', por favor escribe cuáles (separadas por comas). No te olvides de incluir a tu organización.")
    compromiso_convencionales = models.BooleanField("Convencionales comprometidos",
        default=False,
        help_text="¿Tu propuesta cuenta con compromisos formales de apoyo de convencionales constituyentes?")
    comvencionales_comprometidos = models.ManyToManyField(Constituyente,
        related_name="convencionales_comprometidos",
        verbose_name="Nombres Convencionales Comprometidos",
        blank=True,
        help_text="Si tu respuesta fue 'sí', por favor escribe cuáles (separadas por comas). No te olvides de incluir a tu organización.")
    anexo_propuesta = models.FileField(upload_to='documents/',
        verbose_name="Anexos de la Propuesta",
        null=True,
        blank=True)
    titulo = models.CharField("Título Propuesta", max_length=255, null=True)
    class Meta:
        verbose_name = "Propuesta Ciudadana"
        verbose_name_plural = "Propuestas Ciudadanas"
    def __str__(self):
        return self.titulo
