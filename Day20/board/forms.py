from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=2, strip=True)
    keyword = forms.CharField(min_length=1, max_length=10)
    email = forms.EmailField()
    class Meta : 
        model = Article
        # fields = '__all__'
        # model 중에 필요한 애들만
        # fields = ('title', 'content')
        exclude = ['date']