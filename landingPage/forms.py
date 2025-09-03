# forms.py
from django import forms

class StatisticsFilterForm(forms.Form):
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    sector = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. HealthTech', 'class': 'form-control'})
    )
    industry = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Fintech', 'class': 'form-control'})
    )
