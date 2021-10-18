from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Aircraft, Mod

class AircraftForm(ModelForm):
    class Meta:
        model = Aircraft
        fields = ['serial_number', 'tail_number', 'mods']

    mods = ModelMultipleChoiceField(queryset=Mod.objects.all(), widget=CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(AircraftForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        if 'instance' in kwargs:
            self.fields['serial_number'].widget.attrs.update({'readonly': True})
            self.fields['tail_number'].widget.attrs.update({'readonly': True})
            

class ModForm(ModelForm):
    class Meta:
        model = Mod
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ModForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})