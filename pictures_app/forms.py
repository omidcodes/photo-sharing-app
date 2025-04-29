from django import forms
from .models import PictureModel, Comment, Rating

class PictureForm(forms.ModelForm):
    class Meta:
        model = PictureModel
        fields = ['title', 'caption', 'location', 'people_present', 'picture_url']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']
        widgets = {
            'score': forms.Select(choices=[(i, f"{i} ★") for i in range(1, 6)])
        }

        from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Add a comment...',
                'class': 'form-control'
            })
        }
