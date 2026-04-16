from django.db import models

class Solicitud(models.Model):
    TIPO_SOLICITUD_CHOICES = [
        ('academica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('tecnica', 'Técnica'),
        ('otra', 'Otra'),
    ]
    
    nombre_solicitante = models.CharField(max_length=150, verbose_name='Nombre del Solicitante')
    documento_identidad = models.CharField(max_length=50, verbose_name='Documento de Identidad')
    correo_electronico = models.EmailField(verbose_name='Correo Electrónico')
    telefono_contacto = models.CharField(max_length=20, verbose_name='Teléfono de Contacto')
    tipo_solicitud = models.CharField(max_length=20, choices=TIPO_SOLICITUD_CHOICES, verbose_name='Tipo de Solicitud')
    asunto = models.CharField(max_length=200, verbose_name='Asunto')
    descripcion_detallada = models.TextField(verbose_name='Descripción Detallada')
    fecha_solicitud = models.DateField(verbose_name='Fecha de la Solicitud')
    archivo_adjunto = models.FileField(upload_to='solicitudes/', blank=True, null=True, verbose_name='Archivo Adjunto')
    
    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        ordering = ['-fecha_solicitud']
    
    def __str__(self):
        return f"{self.nombre_solicitante} - {self.asunto}"
