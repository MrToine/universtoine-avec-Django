import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField('date de création')
    
    def __str__(self):
        return self.name
    
    @admin.display(
        boolean=True,
        ordering='created_at',
        description="Publié récement ?",
    )
        
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now
    

class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.content
    

    