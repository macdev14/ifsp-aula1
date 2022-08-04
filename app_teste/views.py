from django.shortcuts import render
from .models import Aluno
# Create your views here.
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from .forms import AlunoForm

class IndexView(TemplateView):
    template_name = "index.html"

class CreateAluno(CreateView):
    template_name = "cadastro.html"
    model = Aluno
    form_class = AlunoForm

class UpdateAluno(UpdateView):
    template_name = "atualizar.html"
    model= Aluno
    form_class = AlunoForm

class ListAluno(ListView):
    pagination = 10
    template_name = "list_alunos.html"
    model = Aluno
