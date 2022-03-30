from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.ManyToManyField(User,blank=True,related_name='likes')
    image = models.ImageField(null=False,blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Image,on_delete=models.CASCADE)

class Profile(models.Model):
    username = models.CharField(max_length =30)
    description = models.TextField(null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name="posts")
    def __str__(self):
       return self.description 

class Comment(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Image,on_delete=models.CASCADE,related_name="comments")
    content = models.TextField()
    
    def __str__(self):
        return str(self.username.username)
    