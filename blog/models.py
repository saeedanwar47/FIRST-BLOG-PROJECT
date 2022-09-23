from django.db import models


# Create your models here.

# category model
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Title


# post model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')

    def __str__(self):
        return self.Title
