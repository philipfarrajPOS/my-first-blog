from django.contrib import admin
from .models import Post


# Register your models here.

admin.site.register(Post)
posts1 = Post.objects.filter().order_by('published_date')
