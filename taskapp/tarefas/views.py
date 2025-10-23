from django.shortcuts import render, redirect
from django.contrib import messages
from .models import tbltarefas
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.models import User




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # autentica o usuário na sessão
            return redirect('pagina_inicial')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'index.html')

def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existe.')
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Cadastro efetuado com sucesso. Faça login.')
                return redirect('login')
        else:
            messages.error(request, 'Preencha todos os campos.')

    return render(request, 'cadastro.html')


#def criar_tarefa_view(request):
    # Verifica se o usuário está logado
   # if 'usuario_id' not in request.session:
    #    return redirect('login')

    # Se for POST, cria a tarefa (aqui você vai depois conectar com o model de tarefas)
   # if request.method == 'POST':
        # Aqui futuramente você vai receber dados da tarefa
   #     return redirect('criar_tarefa')

    # Renderiza a tela de criação de tarefa
   # return render(request, 'criarTarefa.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



# Página inicial – mostra as tarefas do usuário

@login_required
def pagina_inicial(request):
    tarefas = tbltarefas.objects.filter(usuario=request.user).order_by('data_conclusao')
    return render(request, 'pagina_inicial.html', {'tarefas': tarefas})

# Criar nova tarefa
@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        status = request.POST.get('status')
        data_conclusao = request.POST.get('data')

        if titulo:
            tbltarefas.objects.create(
                usuario=request.user,
                titulo=titulo,
                descricao=descricao,
                status=status,
                data_conclusao=data_conclusao or None
            )
            return redirect('pagina_inicial')

    return render(request, 'criarTarefa.html')

# Editar tarefa existente

@login_required
def editar_tarefa(request, id):
    tarefa = get_object_or_404(tbltarefas, id=id, usuario=request.user)

    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.status = request.POST.get('status')
        tarefa.data_conclusao = request.POST.get('data') or None
        tarefa.save()
        return redirect('pagina_inicial')

    return render(request, 'criarTarefa.html', {'tarefa': tarefa, 'editando': True})

# Marcar como concluída
@login_required
def concluir_tarefa(request, id):
    tarefa = get_object_or_404(tbltarefas, id=id, usuario=request.user)
    tarefa.status = 'concluida'
    tarefa.data_conclusao = timezone.now().date()
    tarefa.save()
    return redirect('pagina_inicial')
# Deletar tarefa
@login_required
def deletar_tarefa(request, id):
    tarefa = get_object_or_404(tbltarefas, id=id, usuario=request.user)
    tarefa.delete()
    return redirect('pagina_inicial')




# Create your views here.

