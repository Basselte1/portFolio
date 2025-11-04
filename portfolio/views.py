from datetime import datetime

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from config import settings
from portfolio.models import Service, Projet, Client, Technologie, MessageContact


# Create your views here.

#fonnction pour la page d'accueil


def home(request):

    services = Service.objects.all()
    date = datetime.today()

    if request.method == "POST":
        nom = request.POST.get('nom')
        adresse = request.POST.get('adresse')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')  # si tu ajoutes ce champ
        message = request.POST.get('message')

        print("Données reçues :", nom, email, message, adresse, telephone)  # Debug

        if not nom or not email or not message or not adresse or not telephone:
            messages.error(request, " Veillez remplir tous les champs.")
            return render(request, 'index.html',{'services' : services,'date':date})  # Afficher la page avec les erreurs

        # ✅ Enregistrement dans la base de données
        MessageContact.objects.create(
            nom=nom,
            adresse=adresse,
            email=email,
            telephone=telephone,
            message=message
        )

        # ✅ Envoi de l'email à l’administrateur
        sujet = f"Nouveau message de {nom} via le formulaire de contact"
        contenu = f"""
    Nom : {nom}
    Adresse : {adresse}
    Email : {email}
    Téléphone : {telephone}

    Message :
    {message}
            """

        print("en cour d'envoie")

        try:
            send_mail(
                sujet,
                contenu,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False
            )
            print("envoir reussi")

            # ✅ Envoi de confirmation à l’utilisateur
            sujet_user = "Confirmation de réception de votre message"
            contenu_user = f"""
            Bonjour {nom},

            Nous avons bien reçu votre message et vous remercions de nous avoir contactés.

            Voici un résumé de votre demande :

            Adresse : {adresse}
            Téléphone : {telephone}
            Message :
            {message}

            Nous vous répondrons dans les plus brefs délais.

            Bien cordialement,
            L’équipe {settings.NOM_ENTREPRISE if hasattr(settings, 'NOM_ENTREPRISE') else 'Support'}.
                        """
            send_mail(
                sujet_user,
                contenu_user,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False
            )
            messages.success(request, "Merci de votre confiance, nous vous contacterons dans de bref delai !")
        except:
            messages.error(request, "Une erreur est survenue lors de l'envoi du message.")

        return redirect('home')  # Rester sur la même page


    return render(request, 'index.html',{'services' : services,'date':date})


def envoyer_email_notification(self, demande, statut):
        """
        Envoie un email au client lorsque sa demande est validée ou refusée.
        - Paramètres :
            - demande : L'objet DemandeService concerné
            - statut : "validée" ou "refusée"
        """
        sujet = f"Votre demande a été recue"
        message = f"""
        Bonjour M/Mme {MessageContact.nom},

        Votre requete est encour de traitement .

        Merci de votre confiance.
        """
        # Envoi de l'email au client
        send_mail(sujet, message, settings.DEFAULT_FROM_EMAIL, [MessageContact.email])


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

def imc(request):
        return render(request, 'imc.html')

###################################################################################

'''def contact_view(request):
    print("Méthode reçue :", request.method)  # Debug

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        adresse = request.POST.get("adresse")
        message = request.POST.get("message")
        telephone = request.POST.get("telephone")

        print("Données reçues :", name, email, message,adresse,telephone)  # Debug


        if not name or not email or not message or not adresse or not telephone:
            messages.error(request, " Veillez remplir tous les champs.")
            return render(request, "home/contact.html")  # Afficher la page avec les erreurs

        try:
            send_mail(
                subject=f"Message de {name} depuis le formulaire de contact",
                message=f"Nom: {name}\nEmail: {email}\nMessage: {message}\nadresse: {adresse}",
                from_email=email,
                recipient_list=['edjabeadam1@gmail.com'],  # Mets ton email ici
                fail_silently=False,
            )
            messages.success(request, "Merci de votre confiance, nous vous contacterons dans de bref delai !")
            return render(request, "home/contact.html", {"show_modal": True})  # Affichage de la modal

        except Exception as e:
            messages.error(request, "Erreur lors de l'envoi du message. Veillez réessayez.")
            return render(request, "home/contact.html")

    return render(request, "home/contact.html")  # Charge la page avec le formulaire'''

