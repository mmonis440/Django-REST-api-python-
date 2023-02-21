from django.db import models
from django.utils import timezone
import datetime
from datetime import date

# Create your models here.

class question(models.Model):
    question_text=models.CharField(max_length=200)
    publication_date=models.DateField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now =timezone.now()
        return now - datetime.timedelta(days=1) <= self.publication_date <= now


class choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
