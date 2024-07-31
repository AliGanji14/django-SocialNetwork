from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('home:post_detail', args=[self.id, self.slug])
