from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Proveedore

class ProveedoreForm(forms.ModelForm):
    class Meta:
        model = Proveedore
        fields = ('nit', 'nombre_empresa', 'direccion', 'telefono', 'fax', 'correo_empresa', 'nombre_contacto',
                  'apellido_contacto', 'telefono_contacto', 'correo_contacto')
        
