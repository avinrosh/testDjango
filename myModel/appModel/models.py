from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    name=models.ForeignKey(Topic)
    url=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.name

class Accessdata(models.Model):
    date=models.DateField()
