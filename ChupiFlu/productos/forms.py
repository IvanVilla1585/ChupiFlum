from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import ProductoTerminado

class ProductoTerminadoForm(forms.ModelForm):
    class Meta:
        model = ProductoTerminado
        fields = ('nombre', 'descripcion', 'categoria', 'costo_produccion', 'precio_venta',)
