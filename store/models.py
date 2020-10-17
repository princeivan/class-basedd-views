from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)


    class Meta:
        db_table = 'book'


    def __str__(self):
        return self.name

