from django.conf import settings
from django.db import models
from django.utils import timezone

## defines our model (class)
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
 ## publish method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

## returns title as string of text
    def __str__(self):
        return self.title


