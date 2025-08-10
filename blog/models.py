from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    summary = models.TextField()
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

