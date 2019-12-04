from django import forms
# from django.db import models
from .models import Article, Comment

# django forms valdation
class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=2, strip=True)
    email = forms.EmailField()
    keyword = forms.CharField(min_length=1, max_length=10)
    # date = forms.DateTimeField()
    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ['date',]