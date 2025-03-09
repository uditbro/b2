from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    topics = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.topics
    

class Entry(models.Model):
    text = models.ForeignKey(Topic, on_delete=models.CASCADE)
    entries = models.TextField(null= False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        return f"{self.entries[:50]}"
    
class Picture(models.Model):
    picture = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ImageField(default="",blank=True)

    

    