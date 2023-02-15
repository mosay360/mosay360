from distutils.command.upload import upload
from email.policy import default

from django import forms
from django.forms import ModelForm, widgets
from .models import Post
from .models import Comment

# create a post form


choices = [('coding', 'coding'), ('sport', 'sport'), ('programming', 'programming'), ]







class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'author',
                   'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            #'category': forms.Select(choices= choices, attrs={'class': 'form-control'}),
           # 'blogImage':forms.ImageField(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            
        }


class EditForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug',  'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            #'category':forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email= forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email', 'body')
        
    widgets = {
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),
        'body': forms.Textarea(attrs={'class':'form-control'}),
    }
class SearchForm(forms.Form):
    query = forms.CharField()