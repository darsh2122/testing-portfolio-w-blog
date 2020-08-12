from django.db import models
from django.urls import reverse 
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 20)
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    overview = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={
            'id':self.id
        })