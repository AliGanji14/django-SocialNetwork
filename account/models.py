from django.db import models
from django.contrib.auth import get_user_model


class Relation(models.Model):
    from_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='followers')
    to_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} following {self.to_user}"
