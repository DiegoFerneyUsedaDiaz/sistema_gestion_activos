from django import forms
from .models import Activos

class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activos
        fields = ['nombre', 'marca', 'modelo', 'fecha_adquisicion', 'valor', 
                  'Tipo_activo', 'Ubicacion', 'Estado', 'Empleado']
