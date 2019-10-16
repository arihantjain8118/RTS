from django import forms
from .models import Ticket

class ticket(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = ('passenger_name', 'age', 'date')