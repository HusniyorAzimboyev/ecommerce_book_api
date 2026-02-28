from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()

    def __str__(self):
        return self.name
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre,on_delete=models.SET_NULL,null=True)
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)
    pdf = models.FileField(upload_to='books/pdfs/', null=True, blank=True)
    pages = models.SmallIntegerField()
    description = models.TextField()
    price = models.SmallIntegerField(null=False,blank=False)
    stock = models.SmallIntegerField()

    def increase_stock(self,quantity):
        self.stock+=quantity
        self.save()
        return f"Increased to {self.stock}"
    def reduce_stock(self,quantity):
        self.stock-=quantity
        self.save()
        return f'Reduced to {self.stock}'
    def __str__(self):
        return f'{self.title}({self.stock})'
