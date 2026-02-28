from django.db import models

class QuestionsAsked(models.Model):
    time = models.DateTimeField()
    topic = models.CharField(max_length=200)
    ai_answer = models.TextField()

    def __str__(self):
        return self.prompt