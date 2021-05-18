from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 2000)
    pub_dated = models.DateTimeField('data published')
    body = models.TextField()
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]