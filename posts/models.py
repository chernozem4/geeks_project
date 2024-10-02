from django.db import models
from django.utils.translation.trans_null import npgettext


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null = True)
    is_active= models.BooleanField(default=True, null = True)
    view_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title




