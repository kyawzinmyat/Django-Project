from django.db import models
from Courses.models import Course


# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
		
	class Meta:
		abstract = True
	def get_name(self):
		return self.name
	
class Student(Person):
	gpa = models.IntegerField(null=True)
	num_of_course = models.IntegerField(default=0)
	courses = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
	
class Teacher(Person):
	degree=models.CharField(max_length=120,null=True)
	courses = models.OneToOneField(Course,on_delete=models.CASCADE,null=True)
	
	
#python manage.py runserver
		
	
	