from django.contrib import admin
from .models import Article

# Register your models here.

# Article 등록 (Db)처럼 사용하는 녀석
admin.site.register(Article)