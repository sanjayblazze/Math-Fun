from django.db import models
from embed_video.fields import EmbedVideoField

class AllStandard(models.Model):
    clsimg = models.ImageField(upload_to='classimg/', blank=True)
    standardname = models.CharField(max_length=300)
    deskrip = models.CharField(max_length=20000)

    def __str__(self):
        return self.standardname

class Topic(models.Model):
    Topicname = models.ForeignKey(AllStandard, on_delete=models.CASCADE)
    tname = models.CharField(max_length=300)
    files = models.FileField(upload_to='pdfs/')
    video = EmbedVideoField(blank=True)

    def __str__(self):
        return self.tname

class Weightage(models.Model):
    image = models.ImageField(upload_to = 'images/',blank = True)
    weight = models.TextField(max_length=5000)
    def __str__(self):
        return self.weight

