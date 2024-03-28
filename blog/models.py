from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(verbose_name="sarlavha", max_length=150)
    subtitle = models.CharField( max_length=250)
    body = models.TextField(verbose_name="content qismi")
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    image = models.ImageField( upload_to='article_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
        
    