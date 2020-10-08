from django.db import models

class AllStandard(models.Model):
    clsimg = models.ImageField(upload_to='classimg/', blank=True)
    standardname=models.CharField(max_length=300)
    def __str__(self):
        return self.standardname

class Topic(models.Model):
    Topicname=models.ForeignKey(AllStandard, on_delete=models.CASCADE)
    tname=models.CharField(max_length=300)
    files = models.FileField(upload_to='pdfs/')
    def __str__(self):
        return self.tname

class Weightage(models.Model):
    image = models.ImageField(upload_to = 'images/',blank = True)
    weight=models.TextField(max_length=5000)
    def __str__(self):
        return self.weight
