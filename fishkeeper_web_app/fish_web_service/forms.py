from django import forms
from .models import Fish

class FishForm(forms.ModelForm):
    class Meta:
        model = Fish
        fields = ['name', 'type', 'description', 'habitat', 'requirements', 'food', 'compatibility', 'photos_count']
        widgets = {
            'compatibility': forms.TextInput(attrs={'placeholder': 'Optional'}),
        }
