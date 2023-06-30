from django.forms import ModelForm
from .models import Korisnici, Predmeti, Upisi
from django.contrib.auth.hashers import make_password
from django import forms
from django.forms import PasswordInput

class UserForm(ModelForm):
    password = forms.CharField(widget=PasswordInput)
    class Meta:
        model = Korisnici
        fields = ['first_name', 'last_name','username', 'email', 'password', 'uloga', 'status']
        labels = {
            'first_name': 'Ime',
            'last_name': 'Prezime',
            'username': 'Korisničko ime',
            'email': 'E-mail',
            'password': 'Lozinka',
            'uloga': 'Uloga',
            'status': 'Status',
        }
    def clean_password(self):
        password = make_password(self.cleaned_data.get('password'))
        return password
    
class SubjectForm(ModelForm):
    class Meta:
        model = Predmeti
        fields = ['name', 'kod', 'program', 'ects', 'sem_red', 'sem_izv', 'izborni', 'nositelj']
        labels = {
            'name': 'Naziv',
            'kod': 'Kod',
            'program': 'Program',
            'ects': 'ECTS',
            'sem_red': 'Semestar redoviti',
            'sem_izv': 'Semestar izvanredni',
            'izborni': 'Izborni',
            'nositelj': 'Nositelj',
        }
    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        self.fields['nositelj'].queryset = Korisnici.objects.filter(uloga='PROF')
