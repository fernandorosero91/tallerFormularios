from django.contrib import admin
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'documento_identidad', 'fecha_asistencia', 'hora_ingreso', 'hora_salida', 'presente', 'tiene_observaciones']
    list_filter = ['presente', 'fecha_asistencia']
    search_fields = ['nombre_completo', 'documento_identidad', 'correo_electronico']
    date_hierarchy = 'fecha_asistencia'
    ordering = ['-fecha_asistencia', '-hora_ingreso']
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre_completo', 'documento_identidad', 'correo_electronico')
        }),
        ('Detalles de Asistencia', {
            'fields': ('fecha_asistencia', 'hora_ingreso', 'hora_salida', 'presente')
        }),
        ('Observaciones', {
            'fields': ('observaciones',),
            'classes': ('collapse',)
        }),
    )
    
    def tiene_observaciones(self, obj):
        return "✓ Sí" if obj.observaciones else "✗ No"
    tiene_observaciones.short_description = 'Observaciones'
