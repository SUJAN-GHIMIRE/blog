from blog_app.models import BlogPost,CommentOnPost
from django import forms


class BlogPostForm(forms.ModelForm):
    class Meta():
        model = BlogPost
        
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs= {'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class CommentOnPostForm(forms.ModelForm):
    class Meta():
        model = CommentOnPost
        fields = ('comment_author','comment_text')


        widgets = {
            'comment_author':forms.TextInput(attrs= {'class':'textinputclass'}),
            'comment_text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
