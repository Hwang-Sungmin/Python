from django.db import models

# Create your models here.

#charfield는 길이를 반드시 설정
class Board(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=32)
    contents = models.TextField()
    creator = models.CharField(max_length=16)

    
