from django.db import models

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length = 50)
	nation = models.CharField(max_length = 50)
	vision = models.CharField(max_length = 100)
	weapon = models.CharField(max_length = 50)

	def __str__(self):
		return(f"{self.name}")