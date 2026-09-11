# =====================================================================
# portfolio/views.py
# =====================================================================
from datetime import datetime

from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from config import settings
from portfolio.models import Service, Projet, Client, Technologie, MessageContact

#function pour la page d'accueil

def home(request):
    """
        enregistre les informations des clients dans la BD
        params:
            request: requete de l'utilisateur
        return:
            mail a l'utilisateur + redirection sur la page d'accueil
    """
    services = Service.objects.all()
    date = datetime.today()

    if request.method == "POST":
        nom = request.POST.get('nom')
        adresse = request.POST.get('adresse')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')  
        message = request.POST.get('message')

        print("Données reçues :", nom, email, message, adresse, telephone)  # Debug

        if not nom or not email or not message or not adresse or not telephone:
            messages.error(request, " Veillez remplir tous les champs.")
            return render(request, 'index.html',{'services' : services,'date':date}) 
        
        # Enregistrement dans la base de données
        MessageContact.objects.create(
            nom=nom,
            adresse=adresse,
            email=email,
            telephone=telephone,
            message=message
        )

        # Envoi de l'email à l’administrateur
        sujet = f"Nouveau message de {nom} via le formulaire de contact"
        context_email = {

        "nom"        : nom,
        "adresse"    : adresse,
        "email"      : email,
        "telephone"  : telephone,
        "message"    : message ,
        "annee"      : datetime.today().year,
        "nom_developpeur" :getattr(settings, "NOM_DEVELOPPEUR", "AdamDev"),
        "telephone_developpeur" : getattr(settings, "TELEPHONE_DEVELOPPEUR",) 
        }
         
        print("en cour d'envoie")

        contenu_html = render_to_string(
             "emails/notification_admin.html",
             context_email,
        )

        contenu_text = f"""
            Nouveau message reçu depuis votre site.

            nom : {nom}
            adresse : {adresse}
            email : {email}
            telephone : {telephone}

            message :
            {message}
            """
        
        try:
            email_admin = EmailMultiAlternatives(
                subject    = sujet,
                body       = contenu_text,
                from_email = settings.DEFAULT_FROM_EMAIL,
                to         = [settings.ADMIN_EMAIL],
            
            )

            email_admin.attach_alternative(
                 contenu_html,"text/html"
            )
            email_admin.send()
        except Exception as e:
             
            print("erreur lors de l'envoit d u message", e)
            messages.error(request, "Une erreur est survenue lors de l'envoi du message.")


            # Envoi de confirmation à l’utilisateur
        sujet_client = "Confirmation de réception de votre requete"

        context_email_client = {

                "nom"        : nom,
                "adresse"    : adresse,
                "email"      : email,
                "telephone"  : telephone,
                "annee"      : datetime.today().year,
                "nom_developpeur" : getattr(
                    settings, "NOM_DEVELOPPEUR", "AdamDev",
                ),
                "telephone_developpeur" : getattr(settings, "TELEPHONE_DEVELOPPEUR"),
                "email_developpeur" : settings.ADMIN_EMAIL,
                
            }
        
        context_text_client = f"""

                Bonjour M./Mme {nom},

                Votre message a été bien reçu.

                vous aurez un retour dans les meilleurs délais.

                Email : {email}
                Téléphone : {telephone}

                Merci pour votre confiance.

            """

        context_client_html = render_to_string(
            "emails/confirmation_client.html",
            context_email_client,
            )
        try:
            email_client = EmailMultiAlternatives (
                subject  = sujet_client,
                body     = context_text_client,
                from_email= settings.DEFAULT_FROM_EMAIL,
                to=[email],

                )
            email_client.attach_alternative(
                context_client_html, "text/html",
                )
            email_client.send()

            messages.success(request, "Merci de votre confiance, nous vous contacterons dans de bref delai !")
        except:
            messages.error(request, "Une erreur est survenue lors de l'envoi du message.")

        return redirect('home') 


    return render(request, 'index.html',{'services' : services,})

################################################################################################################

def projet(request):
    projets = Projet.objects.all()
    return render(request, 'projet.html',{'projets' : projets})

def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html',{'clients' : clients})

def technologies(request):
    technologie = Technologie.objects.all()
    return render(request, 'technologies.html',{'technologie' : technologie})

def apropos(request):
        return render(request, 'home/apropos.html')

###################################################################################
