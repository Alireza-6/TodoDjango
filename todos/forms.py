from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a new task...', 'id': 'taskInput'})
    )
