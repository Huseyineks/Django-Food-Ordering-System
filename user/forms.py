from App.models import Options,Paying
from django import forms

class OptionsForm(forms.ModelForm):
    class Meta:
        model = Options
        fields = '__all__'

class PayingForm(forms.ModelForm):
    class Meta:
        model = Paying
        fields = '__all__'
