from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from .models import Pacientes

def pacientes(request):
    if request.method == "GET":
        pacientes_list = Pacientes.objects.all()
        return render(request, 'pacientes.html', {'queixas': Pacientes.choices_queixa, 'pacientes': pacientes_list})
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0 or not foto:
            messages.add_message(request, constants.ERROR, 'O campo nome e foto são obrigatórios')
            return redirect('pacientes')

        paciente = Pacientes(
            nome=nome,
            email=email,
            telefone=telefone,
            queixa=queixa,
            foto=foto
        )
        paciente.save()

        messages.add_message(request, constants.SUCCESS, 'Paciente adicionado com sucesso')
        return redirect('pacientes')
    
def paciente_view(request, id):
    paciente = Pacientes.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'paciente.html', {'paciente': paciente})

def atualizar_paciente(request, id):
    pagamento = request.POST.get('pagamento')
    paciente = Pacientes.objects.get(id=id)

    if pagamento == 'ativo':
        paciente.pagamento = True
        paciente.save()
    else:
        paciente.pagamento = False
        paciente.save()
    return render(request, 'paciente.html', {'paciente': paciente})