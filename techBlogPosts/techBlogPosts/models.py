from ast import Str
from django.db import models

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    cmpny_code = models.CharField(max_length=200)
    post_id = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    in_date = models.DateTimeField()

    def __str__(self):
        return self.title