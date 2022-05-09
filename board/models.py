from django.db import models
from django.urls import reverse
from accounts.models import User
from datetime import datetime
from uuid import uuid4

# Create your models here.

USER_TYPE = (
    (0, 'Agency'),
    (1, 'Company')
)


def get_file_path(instance, _):
    path = 'Agency' if isinstance(instance, Announcement) else 'Company'

    ymd_path = datetime.now().strftime("%Y/%m/%d")
    uuid_name = uuid4().hex
    return '/'.join([path, ymd_path, uuid_name])


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    process = models.IntegerField(default=0)
    deadline = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Board'

    def get_absolute_url(self):
        return reverse('board_detail', args=[str(self.id)])


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Comment'


class File(models.Model):
    name = models.CharField(max_length=256)
    uploadFile = models.FileField(upload_to=get_file_path)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'File'


class Announcement(File):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Announcement'


class Estimate(File):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Estimate'


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Question'


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Answer'
