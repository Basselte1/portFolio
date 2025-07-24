from django.contrib import admin

#Affichage des MODELS dans ADMIN #####################################################################

class AdminService(admin.ModelAdmin):
    list_display = ('nom', 'date_creation')
    search_fields = ('nom','description')

##################################################################################################################
class AdminProjet(admin.ModelAdmin):
    list_display = ('titre','date_creation')
    search_fields = ('nom',)

class AdminClient(admin.ModelAdmin):
    list_display = ('nom','date_creation')
    search_fields = ('nom',)

class AdminTechnologie(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)



class MessageContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'date')
    search_fields = ('nom', 'email', 'message')

from portfolio.models import Service, Projet, Client, Technologie, MessageContact

# Register your models here.

admin.site.register(Service,AdminService)
admin.site.register(Projet,AdminProjet)
admin.site.register(Client,AdminClient)
admin.site.register(Technologie, AdminTechnologie)
admin.site.register(MessageContact, MessageContactAdmin)