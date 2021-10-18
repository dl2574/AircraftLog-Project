from django.forms import ModelForm
from .models import Discrepancy

class DiscrepancyForm(ModelForm):
    class Meta:
        model = Discrepancy
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DiscrepancyForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})