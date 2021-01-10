from django.db import models

# Create your models here.
class Author(models.Model):
    # Id = models.IntegerField(default=0)
    Email = models.EmailField(max_length=200)
    Name = models.CharField(max_length=200)
    Birthday = models.DateTimeField()
    Address = models.CharField(max_length=200)
    Telephone = models.CharField(max_length=11)
    Created = models.DateTimeField()
    Modified = models.DateTimeField()

class Book(models.Model):
    # Id = models.IntegerField(default=0)
    Title = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Created = models.DateTimeField()
    Modified = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)