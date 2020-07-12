from django.db import models

class Snippet(models.Model):
    file = models.ImageField()
    email = models.EmailField()
