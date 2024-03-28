from django.contrib import admin
from .models import Category, Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id',  'title','views', 'category', 'created_at' )
    readonly_fields = ['views']
    
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)