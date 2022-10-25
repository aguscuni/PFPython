from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class JugadorFormulario(forms.Form):

    name = forms.CharField()
    surname = forms.CharField()
    position = forms.CharField()
    country = forms.CharField()
    birth = forms.DateField()


class EntrenadorFormulario(forms.Form):

    name = forms.CharField()
    surname = forms.CharField()
    country = forms.CharField()
    birth = forms.DateField()


class EquipoFormulario(forms.Form):

    name = forms.CharField()
    country = forms.CharField()
    foundation_year = forms.IntegerField()


class UserEditionForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Primer Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        # help_texts = {k: "" for k in fields}
