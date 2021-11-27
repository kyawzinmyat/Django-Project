from django.db import models

# Create your models here.

class Test(models.Model):
    description = models.TextField()

class Artist(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    
    def get_name(self):
    	return self.name
    	

class Album(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,null=True)
    price = models.IntegerField()


