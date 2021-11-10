from django import forms


class Contact (forms.Form):
    message = forms.CharField(
        label='Mensaje', widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}), required=True)
