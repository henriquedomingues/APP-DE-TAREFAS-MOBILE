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
            # Salva o ID do usuário na sessão
            request.session['usuario_id'] = user.id
            return render(request, 'pagina_inicial.html', {'usuario': user})
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


def criar_tarefa_view(request):
    # Verifica se o usuário está logado
    if 'usuario_id' not in request.session:
        return redirect('login')

    # Se for POST, cria a tarefa (aqui você vai depois conectar com o model de tarefas)
    if request.method == 'POST':
        # Aqui futuramente você vai receber dados da tarefa
        return redirect('criar_tarefa')

    # Renderiza a tela de criação de tarefa
    return render(request, 'criarTarefa.html')


def logout_view(request):
    request.session.flush()  # Limpa todos os dados da sessão
    return redirect('login')