from django import forms
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = [
            'nombre_completo',
            'documento_identidad',
            'correo_electronico',
            'fecha_asistencia',
            'hora_ingreso',
            'hora_salida',
            'presente',
            'observaciones'
        ]
        widgets = {
            'nombre_completo': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ingrese su nombre completo'
            }),
            'documento_identidad': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ej: 1234567890'
            }),
            'correo_electronico': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'correo@ejemplo.com'
            }),
            'fecha_asistencia': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
            'hora_ingreso': forms.TimeInput(attrs={
                'class': 'form-input',
                'type': 'time'
            }),
            'hora_salida': forms.TimeInput(attrs={
                'class': 'form-input',
                'type': 'time'
            }),
            'presente': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Observaciones adicionales (opcional)',
                'rows': 4
            })
        }
