from django import forms
from .models import Fish

class FishForm(forms.ModelForm):
    class Meta:
        model = Fish
        fields = ['name', 'habitat', 'type', 'habitat_detail_info', 'description', 'food', 'compatibility', 'photos_count']
        widgets = {
            'compatibility': forms.TextInput(attrs={'placeholder': 'Optional'}),
        }
