from django.db import models

class PictureModel(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField(null=True)
    location = models.CharField(max_length=255, null=True)
    picture_url = models.URLField()

    def __str__(self):
        return self.title