from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SolicitudForm

def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Solicitud enviada exitosamente!')
            return redirect('confirmacion_solicitud')
    else:
        form = SolicitudForm()
    
    return render(request, 'solicitudes/crear_solicitud.html', {'form': form})

def confirmacion_solicitud(request):
    return render(request, 'solicitudes/confirmacion.html')
