from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'nombre_solicitante',
            'documento_identidad',
            'correo_electronico',
            'telefono_contacto',
            'tipo_solicitud',
            'asunto',
            'descripcion_detallada',
            'fecha_solicitud',
            'archivo_adjunto'
        ]
        widgets = {
            'nombre_solicitante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre completo'
            }),
            'documento_identidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 1234567890'
            }),
            'correo_electronico': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com'
            }),
            'telefono_contacto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 3001234567'
            }),
            'tipo_solicitud': forms.Select(attrs={
                'class': 'form-control'
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Resumen breve de su solicitud'
            }),
            'descripcion_detallada': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describa detalladamente su solicitud'
            }),
            'fecha_solicitud': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'archivo_adjunto': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
