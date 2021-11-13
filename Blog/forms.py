from django import forms


class AddBlogs(forms.Form):
    title = forms.CharField(label='Título', max_length=50, required=True)
    content = forms.CharField(label='Contenido', widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 40}), required=True)
    image = forms.ImageField(label='Imagen', required=False)
