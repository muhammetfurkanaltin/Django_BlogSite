from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)  # Blog, Takım vb.
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Content(models.Model):
    CONTENT_TYPES = [
        ('blog-text', 'Blog'),  
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPES)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title