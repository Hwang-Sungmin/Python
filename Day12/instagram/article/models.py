from django.db import models
# image resized를 위해 import
# pip install django-imagekit
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

# Create your models here.

class Article(models.Model):
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 원본 이미지를 저장
    image = models.ImageField(blank=True)
    
    # image resize 수정된 이미지를 저장
    # image_resized = ProcessedImageField(
    #     #source = 'image',
    #     upload_to = 'articles/image',
    #     processors = [ResizeToFill(200, 200)],
    #     format='JPEG',
    #     options = {'quality' : 90}
    # )

    # 이미지 썸네일 생성
    # media/CACHE에 원본 이미지의 썸네일을 자동생성
    #image_thumbnail = ImageSpecField(
    #    source='image',
    #    processors=[Thumbnail(200, 200)],
    #    format='JPEG',
    #    options={'quality':90}
    #)
    def comments(self):
        return Comment.objects.filter(article_id=self.id)
    def article_images(self):
        return ArticleImages.objects.filter(article_id=self.id)

class ArticleImages(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(300, 300)],
        format='JPEG',
        options={'quality':90}
    )

class Comment(models.Model):
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 1 (article) : N (comments)  ->  (참조하는 곳, CASCADE 삭제시 참조하는 view도 같이 삭제됨)
    # _id 가 참조키로 생긴다
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
