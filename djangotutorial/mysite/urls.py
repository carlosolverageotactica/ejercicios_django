"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
# ¡ESTA LÍNEA ES CLAVE! Importa las vistas de la app polls
from polls import views as polls_views

urlpatterns = [
    # Ruta raíz (localhost:8000/)
    path("", polls_views.home, name="home"),
    
    # Ruta del mapa (localhost:8000/mapa)
    path("mapa/", polls_views.mapa, name="mapa"),
    
    # Ruta de la app de encuestas y admin
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

