from django.db import models
from django.utils import timezone
from django.urls import reverse
from user_auth_app.models import UserProfileInfo,User
# from django.conf import settings


# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey(UserProfileInfo, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank = True,null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # def unpublish(self):
    #     self.published_date
    #     self.save()
        
    

    def approve_comments(self):
        return self.comments.filter(approve_comments = True)

    def get_absolute_url(self):
        return reverse("blog_app:blogpost_detail", kwargs={'pk':self.pk})


    def __str__(self):
        return self.title


class CommentOnPost(models.Model):
    comment_post = models.ForeignKey('blog_app.BlogPost',related_name = 'comments', on_delete = models.CASCADE)
    comment_author = models.CharField(max_length = 50)
    comment_text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now())
    approved_comment = models.BooleanField(default = False)


    def approve(self):
        self.approved_comment = True
        self.save()
    

    def get_absolute_url(self):
        return reverse('blogpost_list')

    def __str__(self):
        return self.comment_text




