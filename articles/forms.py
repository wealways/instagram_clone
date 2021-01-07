from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    
    content = forms.CharField(
        label = 'Content',
        widget=forms.Textarea(
            attrs={
                'class':"my-content form-control",
            }
        )
    )

    image = forms.ImageField(
        label = 'Image Upload',
        widget=forms.FileInput(
            attrs={
                'class':"form-control-file"
            }
        )
    )
    class Meta:
        model = Article
        fields = ['content','image',]


class CommentForm(forms.ModelForm):
    
    content = forms.CharField(
        label = '',
        widget=forms.TextInput(
            attrs={
                'class':"my-content form-control",
            }
        )
    )
    
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['article', 'user',]