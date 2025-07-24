from django.db import models

# Create your models here.

class MessageContact(models.Model):
    objects = None
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']  # LIFVIEW

    def __str__(self):
        return self.nom


# ✅ Modèle Catégorie
class Projet(models.Model):
    objects = None
    titre = models.CharField(max_length=255)
    description = models.TextField(default= "")
    date_creation =models.DateField(auto_now_add=True)
    lien = models.URLField(blank=True)

    class Meta:
        ordering = ['titre'] #LIFVIEW
        verbose_name ="Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.titre


###########################################################################

from django.urls import reverse

# ✅ Modèle Services
def get_absolute_url():
    return reverse('home')


class Service(models.Model):
    objects = None
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to= 'images', blank=True, null=True)
    date_creation = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date_creation'] #LIFview
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.nom

class Client(models.Model):
    objects = None
    nom = models.CharField(max_length=255 , verbose_name='Nom client')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to= 'images', blank=True, null=True)
    date_creation = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom

class Technologie(models.Model):
    objects = None
    nom = models.CharField(max_length=255, verbose_name='Nom technologies')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to= 'images', blank=True, null=True)

    def __str__(self):
        return self.nom