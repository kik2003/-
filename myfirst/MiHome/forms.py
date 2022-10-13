from .models import Record
from django.forms import ModelForm, TextInput, TimeInput, DateInput
import datetime

class RecordForm(ModelForm):
    class Meta:
        min_data = datetime.date.today()
        model = Record
        fields = ["name", "number", "time","data"]
        widgets = {
            "name": TextInput(attrs={'data-on-color':  'success','class' :'text'}),
            "number": TextInput(attrs={'input type': 'tel','class' :'text'}),
            "time" : TimeInput(format='%H:%M',attrs={'type': 'time','min':"09:00" ,'max':"18:00"}),
            "data" : DateInput(format='%D',attrs={'type': 'date','class' :'da','min':min_data })
        }
