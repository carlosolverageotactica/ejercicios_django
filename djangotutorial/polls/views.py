from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Opcion, Pregunta
from .formularios import CrearEncuestaForm
from django.utils import timezone




def index(request):
    lista_preguntas_recientes = Pregunta.objects.order_by("-publica_fecha")[:5]
    context = {"lista_preguntas_recientes": lista_preguntas_recientes}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    pregunta = get_object_or_404(Pregunta, pk=question_id)
    return render(request, "polls/detail.html", {"pregunta": pregunta})

def resultados(request, question_id):
    pregunta = get_object_or_404(Pregunta, pk=question_id)
    opciones = list(pregunta.opcion_set.all())
    total_votos = sum(opcion.votos for opcion in opciones)
    for opcion in opciones:
        opcion.porcentaje = round((opcion.votos / total_votos) * 100, 1) if total_votos > 0 else 0
    return render(request, "polls/results.html", {
        "pregunta": pregunta,
        "opciones": opciones,
        "total_votos": total_votos
    })

def voto(request, question_id):
    pregunta = get_object_or_404(Pregunta, pk=question_id)
    try:
        opcion_seleccionada = pregunta.opcion_set.get(pk=request.POST["opcion"])
    except (KeyError, Opcion.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "pregunta": pregunta,
                "error_message": "No seleccionaste ninguna opción.",
            },
        )
    else:
        opcion_seleccionada.votos = F("votos") + 1
        opcion_seleccionada.save()
        return HttpResponseRedirect(reverse("polls:resultados", args=(pregunta.id,)))
    
def home(request):
    return render(request, "polls/home.html")
def mapa(request):
    return render(request, "polls/mapa.html")


#vista nuevo formulario

def crear_encuesta(request):
    if request.method == "POST":
        form = CrearEncuestaForm(request.POST)
        if form.is_valid():
            # 1. Guardar la pregunta en la base de datos
            nueva_pregunta = Pregunta.objects.create(
                pregunta_texto=form.cleaned_data['pregunta_texto'],
                publica_fecha=timezone.now()
            )
            # 2. Guardar las opciones asociadas a esta pregunta
            nueva_pregunta.opcion_set.create(opcion_texto=form.cleaned_data['opcion_1'])
            nueva_pregunta.opcion_set.create(opcion_texto=form.cleaned_data['opcion_2'])
            nueva_pregunta.opcion_set.create(opcion_texto=form.cleaned_data['opcion_3'])
            
            # Redirigir a la lista de encuestas al finalizar
            return HttpResponseRedirect(reverse('polls:index'))
    else:
        form = CrearEncuestaForm()

    return render(request, "polls/crear.html", {"form": form})

#editar encuesta

def editar_encuesta(request, question_id):
    pregunta = get_object_or_404(Pregunta, pk=question_id)
    if request.method == "POST":
        form = CrearEncuestaForm(request.POST)
        if form.is_valid():
            # Actualizar la pregunta
            pregunta.pregunta_texto = form.cleaned_data['pregunta_texto']
            pregunta.save()
            
            # Actualizar las opciones
            opciones = list(pregunta.opcion_set.all())
            if len(opciones) >= 3:
                opciones[0].opcion_texto = form.cleaned_data['opcion_1']
                opciones[0].save()
                opciones[1].opcion_texto = form.cleaned_data['opcion_2']
                opciones[1].save()
                opciones[2].opcion_texto = form.cleaned_data['opcion_3']
                opciones[2].save()
            
            return HttpResponseRedirect(reverse('polls:detail', args=(pregunta.id,)))
    else:
        # Prellenar el formulario con los datos existentes
        opciones = list(pregunta.opcion_set.all())
        initial_data = {
            'pregunta_texto': pregunta.pregunta_texto,
            'opcion_1': opciones[0].opcion_texto if len(opciones) > 0 else '',
            'opcion_2': opciones[1].opcion_texto if len(opciones) > 1 else '',
            'opcion_3': opciones[2].opcion_texto if len(opciones) > 2 else '',
        }
        form = CrearEncuestaForm(initial=initial_data)

    return render(request, "polls/editar.html", {"form": form, "pregunta": pregunta})