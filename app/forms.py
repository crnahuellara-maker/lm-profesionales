from django import forms
from .models import Profesional, Servicio, Entregable

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = '__all__'


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'


class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = '__all__'


class BusquedaServicio(forms.Form):
    nombre = forms.CharField(max_length=100)
