from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from api.models import Book


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name="reviews")
    message = models.TextField(null=True, blank=True)
    rating = models.SmallIntegerField(max_length=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book} - {self.rating}'


class Flashsale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    discount_perc = models.SmallIntegerField(max_length=3)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def is_active(self):
        now = timezone.now()
        return self.start_time <= now <= self.end_time
