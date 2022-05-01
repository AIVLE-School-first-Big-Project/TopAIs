import datetime

from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Board, Comment


class BoardWriteForm(forms.ModelForm):
    def clean_deadline(self):
        deadline = self.cleaned_data['deadline']

        if deadline < datetime.date.today():
            raise forms.ValidationError(_('Invalid date - renewal in past'))

        return deadline

    class Meta:
        model = Board
        fields = ('title', 'content', 'deadline',)


class CommentWriteForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
