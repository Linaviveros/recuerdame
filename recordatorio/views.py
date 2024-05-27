from django.shortcuts import render

# Create your views here.

def lista_recordatorios(request):
    recordatorios = Recordatorio.objects.all()
    return render(request, 'recordatorios/lista_recordatorios.html', {'recordatorios': recordatorios})
