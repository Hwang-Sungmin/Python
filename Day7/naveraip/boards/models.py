from django.db import models

# DB에 클래스명과 같은 녀석의 테이블이 생성
# Create your models here.
class Boards(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    creator = models.CharField(max_length=10, null=True)