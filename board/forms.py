from django import forms
from .models import Board, Comment


class BoardWriteForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'content',)


class CommentWriteForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
