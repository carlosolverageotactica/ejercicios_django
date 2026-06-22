from django import forms

class CrearEncuestaForm(forms.Form):
    pregunta_texto = forms.CharField(
        label="Pregunta de la Encuesta",
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ej. ¿Cuál BD espacial prefieres?',
            'class': 'form-input'
        })
    )
    
    # Definimos 3 campos para opciones iniciales de respuesta
    opcion_1 = forms.CharField(
        label="Opción 1",
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Ej. PostgreSQL+postgis', 'class': 'form-input'})
    )
    
    opcion_2 = forms.CharField(
        label="Opción 2",
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Ej. Arcgis Server/SQL', 'class': 'form-input'})
    )
    
    opcion_3 = forms.CharField(
        label="Opción 3",
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Ej. MongoDB', 'class': 'form-input'})
    )