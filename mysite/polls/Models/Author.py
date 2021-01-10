from django.db import models

class Author:
    def __init__(self, Id, Email, Name, Birthday, Address, Telephone, Created, Modified):
        self.Id = Id
        self.Email = Email
        self.Name = Name
        self.Birthday = Birthday
        self.Address = Address
        self.Telephone = Telephone
        self.Created = Created
        self.Modified = Modified