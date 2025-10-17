from django.shortcuts import render, redirect
from django.contrib import messages
from .models import tblusuarios

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = tblusuarios.objects.get(username=username, password=password)
            return render(request, 'teste.html', {'usuario': user})
        except tblusuarios.DoesNotExist:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'index.html')


def cadastro_view(request):
    # Simple registration view to satisfy URL routing and allow manual testing.
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('password')

        if usuario and senha:
            # Create a new tblusuarios entry (note: passwords stored as plain text here)
            tblusuarios.objects.create(username=usuario, password=senha)
            messages.success(request, 'Cadastro efetuado com sucesso. Faça login.')
            return redirect('login')
        else:
            messages.error(request, 'Preencha todos os campos.')

    return render(request, 'cadastro.html')
