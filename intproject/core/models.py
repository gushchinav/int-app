from django.db import models

class Question(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    question_text = models.CharField(max_length=1000)
    complexity = models.IntegerField()
