from turtle import position
from django import forms


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
