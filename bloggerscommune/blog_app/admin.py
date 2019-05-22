from django.contrib import admin
from blog_app.models import BlogPost,CommentOnPost

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(CommentOnPost)
