from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    cat=models.CharField(max_length=100, blank=False,null=True)
    def __str__(self):
        return self.cat

class Listing(models.Model):
    user=models.CharField(max_length=100, null=True)
    title= models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    current_bid=models.IntegerField(null=True)
    category=models.CharField(max_length=100, null=True)
    image_url=models.URLField(default='google.com')
    sold=models.BooleanField(default=False)
    def __str__(self):
        return self.title


class Comment(models.Model):
    user=models.CharField(max_length=100, null=True)
    title=models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment=models.TextField(null=True)
    def __str__(self) :
        template= '{0.user} {0.title} {0.comment}'
        return template.format(self)
    

class Bid(models.Model):
    user=models.CharField(max_length=100, null=True)
    title=models.ForeignKey(Listing, on_delete=models.CASCADE)
    price=models.IntegerField()
    def __str__(self) :
        template= '{0.user} {0.title} {0.price}'
        return template.format(self)

class WatchList(models.Model):
    name= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item=models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)
    
    def __str__(self) :
        return '{}'.format(self.item)


