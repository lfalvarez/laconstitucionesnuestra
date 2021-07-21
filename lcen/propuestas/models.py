from django.db import models



class Distrito(models.Model):
    distrito = models.CharField("Distrito", max_length=225, unique=True)
    class Meta:
        verbose_name = "Distrito"
        verbose_name_plural = "Distritos"
    def __str__(self):
        return self.distrito



class Comuna(models.Model):
    comuna = models.CharField("Comuna", max_length=225, unique=True)
    distrito_comuna = models.ForeignKey(Distrito, related_name="distrito_comuna", verbose_name="Distrito de la Comuna", null=True, on_delete=models.SET_NULL)
    class Meta:
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"
    def __str__(self):
        return self.comuna
