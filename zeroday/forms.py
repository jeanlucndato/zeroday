from django import forms 
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)
    
    
class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category','subtitle', 'intro', 'body', 'conclusion', 'header_image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'you must write a best hacking article...'}),
            'author': forms.TextInput(attrs={ 'class': 'form-control', 'value':'', 'id': 'elder', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={ 'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'intro': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'conclusion': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        

class EditForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'intro', 'body', 'conclusion', 'header_image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'you must write a best hacking article...'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'intro': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'conclusion': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        
class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}), 
            }