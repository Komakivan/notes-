from django import forms
from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        exclude =['owner']


    def __init__(self,*args,**kwargs):
        super(NotesForm,self).__init__(*args,**kwargs)


        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
