from django import forms
from .models import Post, Autor, Area

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']

class PostForm(forms.ModelForm):
    areas = forms.ModelMultipleChoiceField(queryset=Area.objects.all())

    class Meta:
        model = Post
        fields = ['autores', 'areas', 'titulo', 'texto', 'imagem', 'link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['areas'].widget.attrs['class'] = 'select2'