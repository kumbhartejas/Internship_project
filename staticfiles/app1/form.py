from django import forms
from .models import Section, item

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name']

class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['name', 'description', 'section', 'image', 'price', 'slug','ingredients']
