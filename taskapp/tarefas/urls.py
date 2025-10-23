from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

     path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('criar/', views.criar_tarefa, name='criar_tarefa'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('concluir/<int:id>/', views.concluir_tarefa, name='concluir_tarefa'),
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar_tarefa'),

    
    
]
