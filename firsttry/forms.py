from django import forms
from firsttry.models import empdetails

class empform(forms.ModelForm):
    CodeNo = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Enter your Code Number', 'class' : 'input_bar'}))
    Name = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Enter your Name', 'class' : 'input_bar'}))
    Age = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Enter your Age', 'class' : 'input_bar'}))
    Salary = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Enter your Salary', 'class' : 'input_bar'}))
    Address = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Enter your Address', 'class' : 'input_bar'}))
    Work = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Enter your Work', 'class' : 'input_bar'}))
    class Meta:
        model = empdetails
        fields = '__all__'