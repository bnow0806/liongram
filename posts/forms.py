from dataclasses import field
from secrets import choice
from socket import fromshare
from unicodedata import category
from django import forms

from posts.models import Post

# class PostBaseForm(forms.Form):
#     CATEGORY_CHOICES=[
#         ('1', '일반'),
#         ('2', '계정'),
#     ]
#     image = forms.ImageField(label='이미지')
#     content = forms.CharField(label='내용', widget=forms.Textarea, required=True)
#     category = forms.ChoiceField(label='카테고리', choices = CATEGORY_CHOICES)

class PostBaseForm(forms.ModelForm):
    class Meta:     #Meta?
        model = Post
        fields = '__all__'

class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']
    

class PostUpdateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']


class PostDetailForm(PostBaseForm):
    def __init__(self, *args, **kwargs):    #__init__ 추가 이유?
        super(PostDetailForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['disabled'] = True