from django.db import models



class Propuesta(models.Model):
    autor = models.ForeignKey(User, verbose_name="Autor@ de Propuesta", null=True, on_delete=models.SET_NULL)
    titulo = models.CharField("Título Propuesta", max_length=225)
    cuerpo = models.TextField("Texto Propuesta")
    tipo = models.ForeignKey(TipoPropuesta, related_name="tipo_propuesta", verbose_name="Tipo/Origen Propuesta", null=True, blank=True, help_text="Tipo predefinido de propuesta -individual o colectiva-", on_delete=models.SET_NULL)
    comuna_propuesta = models.ManyToManyField(Comuna, related_name="comuna_propuesta", verbose_name="Comuna/s de Propuesta", help_text="Seleccionar comuna/s si corresponde a una propuesta vinculada a territorio")
    # Si la propuesta es general o tiene alcance nacional
    propuesta_general = models.BooleanField(default=False)
    # Tema principal de tu propuesta
    tema = models.ForeignKey(TemaPropuesta, null=True, on_delete=models.SET_NULL)
    # Tema opcional a añadir cuando no está en los temas ni subtemas predefinidos
    otro_tema = models.CharField("Otro tema", max_length=225, null=True, blank=True)
    # ¿Cuál es el problema que tú o tu organización busca solucionar?
    problema = models.TextField("Descripción de problema a solucionar", null=True, blank=True)
    # Con respecto al problema que planteaste, ¿Cuál sería la situación ideal?
    situacion = models.TextField("Situación ideal de solución", null=True, blank=True)
    # Para lograr esa situación ideal, ¿qué debería contemplar la Nueva Constitución?
    contempla = models.TextField("Lo que debe contemplar la Constitución", null=True, blank=True)
    # Componente de la constitución donde va la propuesta
    componente = models.ManyToManyField(ComponenteConstitucion, verbose_name="Componente de la Constitución")
    # Otro componente si no está en los predefinidos
    otro_componente = models.CharField("Otro Componente", max_length=225, null=True, blank=True)
    # ¿Tu propuesta ya cuenta con compromisos formales de apoyo de convencionales electos? Si/No
    compromiso = models.BooleanField(default=False, verbose_name="Existen compromisos a esta propuesta")
    # Adjunto de compromisos
    adjunto_compromisos = models.FileField(upload_to='documents/', verbose_name="Documento de respaldo de compromisos", null=True, blank=True)
    # Documento de copia de la propuesta
    documento_propuesta = models.FileField(upload_to='documents/', verbose_name="Documento de copia de la Propuesta", null=True, blank=True)
    # Otros antecedentes en documento completo o zip
    anexo_propuesta = models.FileField(upload_to='documents/', verbose_name="Anexos de la Propuesta", null=True, blank=True)
    # Títulos y Cuerpos cortos
    titulo_corto = models.CharField("Título Propuesta Breve", max_length=100, null=True)
    cuerpo_corto = models.CharField("Texto Propuesta Breve", max_length=100, null=True)

    class Meta:
        verbose_name = "Propuesta Ciudadana"
        verbose_name_plural = "Propuestas Ciudadanas"
    def __str__(self):
        return self.titulo
