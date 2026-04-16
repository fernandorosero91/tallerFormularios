from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AsistenciaForm

def registro_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            asistencia = form.save()
            return redirect('asistencia:confirmacion', pk=asistencia.pk)
    else:
        form = AsistenciaForm()
    
    return render(request, 'asistencia/registro.html', {'form': form})

def confirmacion(request, pk):
    from .models import Asistencia
    asistencia = Asistencia.objects.get(pk=pk)
    return render(request, 'asistencia/confirmacion.html', {'asistencia': asistencia})
