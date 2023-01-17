from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import TodoList
# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView
from .forms import TodoListForm, TodoTaskCompleteForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def logout_view(request):
    logout(request)
    return redirect("home")


class TodoListView(LoginRequiredMixin, ListView):
    model = TodoList
    template_name = 'todo.html'
    context_object_name = 'todo'
    form_class = TodoListForm

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['update_form'] = TodoTaskCompleteForm
        return context


class ToDoListCreateView(CreateView):
    model = TodoList
    form_class = TodoListForm
    template_name = 'todo.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('home')


class TodoListUpdate(UpdateView):
    model = TodoList
    form_class = TodoTaskCompleteForm
    context_object_name = 'update_todo_form'
    template_name = 'todo.html'
    success_message = "Task completed"
    success_url = reverse_lazy('home')
