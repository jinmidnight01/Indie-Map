from django.db import models
from django.utils import timezone
from django.conf import settings
from account_app.models import User

# Create your models here.

class Community(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    photo = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    #date = models.DateField(auto_now_add = True) #추가
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content

class Comment(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Community, on_delete = models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.comment



    