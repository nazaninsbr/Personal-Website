from django.db import models

# Create your models here.
class Homepage(models.Model):
	intro_sentence = models.CharField(max_length=100)
	about_me = models.TextField()
	facts_about_me_1 = models.TextField()
	facts_about_me_2 = models.TextField()
	facts_about_me_3 = models.TextField()

class About(models.Model):
	text_1 = models.TextField()
	text_2 = models.TextField()
	text_3 = models.TextField()
	text_4 = models.TextField()
