from django.urls import reverse, reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import ToDoItem, ToDoList

class ListListView(ListView):
    model = ToDoList
    template_name = "to_do_app/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "to_do_app/to_do_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(to_do_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["to_do_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context

class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "to_do_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        to_do_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["to_do_list"] = to_do_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        to_do_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["to_do_list"] = to_do_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.to_do_list_id])

class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "to_do_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["to_do_list"] = self.object.to_do_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.to_do_list_id])

class ListDelete(DeleteView):
    model = ToDoList
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")

class ItemDelete(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["to_do_list"] = self.object.to_do_list
        return context

       