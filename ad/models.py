from django.db import models


class Ad(models.Model):
    title=models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    location=models.CharField(max_length=120)
    date=models.DateTimeField()
    text=models.TextField()
    image=models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title
