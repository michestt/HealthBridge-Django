from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'description',
            'content',
            'pic',
            'tags',
        ]
    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].label='title'
    #     self.fields['description'].label ='description'
    #     self.fields['content'].label ='content'
    #     self.fields['pic'].label ='pic'
    #     self.fields['tags'].label ='tags'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'email',
            'body',
        ]
