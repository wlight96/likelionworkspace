from django.db import models

# Create your models here.
class Oldman_blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]

class Oldman_notice(models.Model):
    notice_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=10)
    student_code = models.IntegerField()
    body = models.TextField()
    def __str__(self):
        return self.notice_title
    def summary(self):
        return self.body[:100]