from django import forms
from .models import Airport, Route

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['from_airport', 'to_airport', 'direction', 'duration', 'position']
        widgets = {
            'from_airport': forms.Select(attrs={'class': 'form-control'}),
            'to_airport': forms.Select(attrs={'class': 'form-control'}),
            'direction': forms.Select(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in minutes'}),
            'position': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
        }

class SearchNthNodeForm(forms.Form):
    start_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    direction = forms.ChoiceField(
        choices=[('left', 'Left'), ('right', 'Right')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    steps = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of steps'})
    )

class ShortestPathForm(forms.Form):
    from_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    to_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )