from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Event
from Aircraft.models import Aircraft

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        
    aircraft = ModelMultipleChoiceField(queryset=Aircraft.objects.all(), widget=CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
