from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def pacientes(request):
    if request.method == "GET":
        return render(request, 'pacientes.html')