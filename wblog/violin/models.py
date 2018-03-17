from django.db import models

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)


class Entry(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	slug = models.SlugField(max_length= 200, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	publish = models.BooleanField(default=True)
	objects = EntryQuerySet.as_manager()
	recording = models.FileField(null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta: 
		verbose_name = "Violin Blog Entry"
		verbose_name_plural = "Violin Blog Entries"
		ordering = ["-created"]
