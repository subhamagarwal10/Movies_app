from django.db import models

# Create your models here.
class movies(models.Model):
	Name = models.CharField(max_length=100)
	Picture = models.CharField(max_length=100)
	Rating = models.IntegerField()
	Notes = models.CharField(max_length=1000)
	
	def __str__(self):
		return "Name: {}".format(self.Name)

class songs(models.Model):
	Movie = models.ForeignKey(movies, on_delete=models.CASCADE)
	Song = models.CharField(max_length=200)
	FileType = models.CharField(max_length=10)
	Singer = models.CharField(max_length=200)
	
	def __str__(self):
		return "Song: {}".format(self.Song)