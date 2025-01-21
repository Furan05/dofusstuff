from django import forms
from .models import Character, Characteristic, BuildRequest

class BuildRequestForm(forms.ModelForm):
    class Meta:
        model = BuildRequest
        fields = []  # We'll handle the fields manually

    character_class = forms.ChoiceField(choices=Character.CLASSES)
    level = forms.IntegerField(min_value=1, max_value=200)
    primary_stats = forms.ModelMultipleChoiceField(
        queryset=Characteristic.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    secondary_stats = forms.ModelMultipleChoiceField(
        queryset=Characteristic.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
