from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
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
        return f'Reduced tp {self.stock}'
    def __str__(self):
        return f'{self.title}({self.stock})'
