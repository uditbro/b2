from django.db import models


class Article(models.Model):
    topic = models.CharField(max_length=255)
    content = models.TextField()
    owner = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.topic