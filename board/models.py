from django.db import models
from accounts.models import User


# Create your models here.

class Board(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    process = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Board'


class Comment(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Comment'
