from django.db import models

class Book:
    def __init__(self, Id, Title, Name, Created, Modified):
        self.Id = Id
        self.Title = Title
        self.Name = Name
        self.Created = Created
        self.Modified = Modified

