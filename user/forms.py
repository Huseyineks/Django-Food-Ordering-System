from App.models import Options,Paying
from django import forms

class OptionsForm(forms.ModelForm):
    # SİZE_CHOİCES = [('Large','Large'),('Medium','Medium'),('Small','Small')]
    # TEMP_CHOİCES = [('Hot','Hot'),('Iced','Iced')]
    # size = forms.ChoiceField(choices=SİZE_CHOİCES ,widget=forms.RadioSelect)
    # temp = forms.ChoiceField(choices=TEMP_CHOİCES ,widget=forms.RadioSelect)
    # request = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Options
        fields = '__all__'

class PayingForm(forms.ModelForm):
    PAYİNG_CHOİCES = [('Online ATM Card','Online ATM Card'),('ATM Card','ATM Card'),('Cash','Cash')]
    paying = forms.ChoiceField(choices=PAYİNG_CHOİCES,widget=forms.RadioSelect)

    class Meta:
        model = Paying
        fields = '__all__'
