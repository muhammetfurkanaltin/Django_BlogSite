from django import forms
from .models import Content
class ContentCreateForm(forms.ModelForm):    # Yontem 2
    class Meta:
        model = Content
        fields = ['title', 'description', 'category', 'content_type', 'author', 'is_active']
        labels = {
            'title': 'Blog Adı',
            'description': 'Açıklama',
            'category': 'Kategori',
            'content_type': 'İçerik Türü',
            'author': 'Yazar',
            'is_active': 'Aktif Mi'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content_type': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        error_messages = {
            'title': {
                'required': 'Blog adı boş bırakılamaz'
            },
            'description': {
                'required': 'Açıklama boş bırakılamaz'
            }
        }