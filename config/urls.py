"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path



admin.site.site_header = "Dashboard"
admin.site.site_title = "Dashboard"
admin.site.index_title = "Welcome Admin"

from config import settings
from portfolio.views import apropos, projet, clients, technologies, home, imc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('apropos/', apropos, name='apropos'),

    path('imc/', imc, name='imc'),
    path('projet/', projet, name='projet'),
    path('client/', clients, name='client'),

    path('technologie/', technologies, name='technologie'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )