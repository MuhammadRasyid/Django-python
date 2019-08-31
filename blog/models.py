from django.db import models

class blog(models.Model):
    judul = models.CharField(max_length=200)
    artikel = models.TextField()
