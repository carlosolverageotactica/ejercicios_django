from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/resultados/
    path("<int:question_id>/resultados/", views.resultados, name="resultados"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.voto, name="voto"),
    path("crear/", views.crear_encuesta, name="crear_encuesta"),
    path("<int:question_id>/editar/", views.editar_encuesta, name="editar_encuesta"), #en cuanto tenga el archivo lo descomento
]
