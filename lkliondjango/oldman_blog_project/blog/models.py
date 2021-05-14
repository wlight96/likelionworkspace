from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

class Notice(models.Model):
    notice_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=10)
    student_code = models.IntegerField()
    body = models.TextField()