from django import forms


class CityDetailForm(forms.Form):
    lat = forms.DecimalField(max_digits=9, decimal_places=6)
    long = forms.DecimalField(max_digits=9, decimal_places=6)
