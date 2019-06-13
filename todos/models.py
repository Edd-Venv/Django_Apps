from datetime import datetime
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title  # this def displays the todotitle on the admin page instead of todoObject


class Bills(models.Model):
    title = models.CharField(max_length=20)
    amount = models.IntegerField()
    created_at = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return '%s %s' % (self.title, self.amount)
