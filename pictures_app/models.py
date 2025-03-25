from django.db import models

class PictureModel(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField()
    location = models.CharField(max_length=255)
    picture_url = models.URLField()

    def __str__(self):
        return self.title