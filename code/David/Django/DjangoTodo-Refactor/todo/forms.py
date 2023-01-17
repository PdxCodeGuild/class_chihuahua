from django import forms
from .models import TodoList


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoListForm(forms.ModelForm):
    due_date = forms.DateField(widget=DateInput())

    class Meta:
        model = TodoList
        fields = ['task_name', 'description', 'due_date']


class TodoTaskCompleteForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['completed']
