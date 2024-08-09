from django.db import models


class Data(models.Model):
    author = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    url = models.CharField(max_length=200)
    publishedAt = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.author