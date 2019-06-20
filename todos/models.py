from datetime import datetime
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title  


class Bills(models.Model):
    title = models.CharField(max_length=20)
    amount = models.PositiveSmallIntegerField(null=True)
    created_at = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return '%s %s' % (self.title, self.amount)
    
    

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    ingredients = models.TextField()
    cook = models.TextField()
    created_at = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
