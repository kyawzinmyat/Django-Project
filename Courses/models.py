from django.db import models
import string
import random


# Create your models here.


class Course_code:
	def __init__(self):
		self.code = self.generate_code()
		
		
	def generate_code(self):
		code =""
		letters = string.ascii_letters
		for i in range(5):
			code += random.choice(letters)
		return code
		
		
		


class Course(models.Model):
	course_name = models.CharField(max_length=100)
	max_student = models.IntegerField()
	current_student_count = models.IntegerField(default=0)
	code = models.TextField(null=True)
	
	def save(self,*args,**kwargs):
		self.code = Course_code()
		super().save(*args,**kwargs)
	

