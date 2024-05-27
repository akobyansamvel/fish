from django import forms
from .models import Fish

class FishForm(forms.ModelForm):
    class Meta:
        model = Fish
        fields = ['name', 'habitat', 'type', 'description', 'habitat_detail_info', 'aquarium_fish_conditions', 'food', 'compatibility', 'photos_count']
        widgets = {
            'compatibility': forms.TextInput(attrs={'placeholder': 'Optional'}),
        }
