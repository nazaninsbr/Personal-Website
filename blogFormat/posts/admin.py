from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "lastupdated" ,"timestamp"]
    list_display_links = ["lastupdated"]
    list_filter = ["lastupdated", "timestamp"]
    search_fields = ["title", "content"]
    list_editable = ["title"]
    class Meta: 
        model = Post 

admin.site.register(Post, PostAdmin)