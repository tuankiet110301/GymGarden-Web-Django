from django.db import models
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



STATUS = (
    (0,"Nháp"),
    (1,"Đã đăng")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.FileField(upload_to='images', default='')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.CharField()
    thumbnail_content = models.TextField(max_length=100, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    views = models.IntegerField(default=0)
    class Meta:
        #Sap xep thu tu bai moi len truoc bai cu xuong duoi '-'
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class PostImage(models.Model):
    image = models.ImageField(upload_to='images')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)






