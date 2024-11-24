from django import forms
from .models import User, Transaction

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'username']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'amount', 'date', 'description', 'type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


