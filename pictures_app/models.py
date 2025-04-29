from django.db import models
from django.contrib.auth.models import User

class PictureModel(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    caption = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    people_present = models.CharField(max_length=255, null=True, blank=True)
    picture_url = models.URLField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(PictureModel, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.picture.title}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(PictureModel, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating {self.score} by {self.user.username} on {self.picture.title}"
