from django.contrib import admin
from .models import Solicitud

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ['nombre_solicitante', 'documento_identidad', 'tipo_solicitud', 'asunto', 'fecha_solicitud', 'tiene_archivo']
    list_filter = ['tipo_solicitud', 'fecha_solicitud']
    search_fields = ['nombre_solicitante', 'documento_identidad', 'correo_electronico', 'asunto']
    date_hierarchy = 'fecha_solicitud'
    ordering = ['-fecha_solicitud']
    readonly_fields = ['fecha_solicitud']
    
    fieldsets = (
        ('Información del Solicitante', {
            'fields': ('nombre_solicitante', 'documento_identidad', 'correo_electronico', 'telefono_contacto')
        }),
        ('Detalles de la Solicitud', {
            'fields': ('tipo_solicitud', 'asunto', 'descripcion_detallada', 'fecha_solicitud')
        }),
        ('Archivo Adjunto', {
            'fields': ('archivo_adjunto',),
            'classes': ('collapse',)
        }),
    )
    
    def tiene_archivo(self, obj):
        return "✓ Sí" if obj.archivo_adjunto else "✗ No"
    tiene_archivo.short_description = 'Archivo Adjunto'
    