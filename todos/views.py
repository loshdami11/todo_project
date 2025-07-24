from django.views.generic import ListView, DetailView,CreateView
from django.urls import reverse_lazy

from .models import Todo



class TodoListView(ListView):
    """List of todos."""
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'


class TodoDetailView(DetailView):
    "A todo."
    model = Todo
    template_name = 'todos/todo_detail.html'

class TodoCreateView(CreateView):
    """Create a todo."""
    model = Todo
    template_name = 'todos/todo_create.html'
    fields = '__all__'  
    success_url = reverse_lazy('home')  