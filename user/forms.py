from App.models import Options
from django import forms

class OptionsForm(forms.ModelForm):
    SİZE_CHOİCES = [('Large','Large'),('Medium','Medium'),('Small','Small')]
    TEMP_CHOİCES = [('Hot','Hot'),('Iced','Iced')]
    size = forms.ChoiceField(choices=SİZE_CHOİCES ,widget=forms.RadioSelect)
    temp = forms.ChoiceField(choices=TEMP_CHOİCES ,widget=forms.RadioSelect)
    request = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Options
        fields = '__all__'
